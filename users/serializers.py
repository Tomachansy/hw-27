from rest_framework import serializers

from avito.settings import EMAIL_DOMAIN_CONSTRAINTS
from users.models import Location, User


class EmailValidator:
    def __call__(self, value):
        if value.endswith(EMAIL_DOMAIN_CONSTRAINTS):
            raise serializers.ValidationError(f"{EMAIL_DOMAIN_CONSTRAINTS} users cannot register.")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    email = serializers.EmailField(validators=[EmailValidator])

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location_id")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            loc_obj, _ = Location.objects.get_or_create(name=location)
            user.location_id.add(loc_obj)

        user.set_password(user.password)
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location_id = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location_id")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            loc_obj, _ = Location.objects.get_or_create(name=location)
            user.location_id.add(loc_obj)

        user.save()
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
