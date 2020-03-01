from rest_framework import serializers
from .models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Contact, Order, OrderItem


class ShopSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=50, verbose_name='Название')
    # url = serializers.URLField(verbose_name='Ссылка', null=True, allow_blank=True)
    # user = serializers.OneToOneField(User, verbose_name='Пользователь',
    #                             allow_blank=True, null=True,
    #                             on_delete=models.CASCADE)
    # state = serializers.BooleanField(verbose_name='статус получения заказов', default=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Shop.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.name)
        instance.code = validated_data.get('url', instance.url)
        instance.linenos = validated_data.get('user', instance.user)
        instance.language = validated_data.get('state', instance.state)
        instance.save()
        return instance

    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'user', 'state')
