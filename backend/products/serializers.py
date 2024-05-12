from rest_framework import serializers
from .models import Product
from .tasks import parce_product_task


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объектов Product.

    Метод create(self, validated_data) - Сохраняет книгу в базе данных
    Метод to_representation(self, instance) - Возвращает словарное
    представление модели
    """
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request_data = self.context['request'].data
        products_count = request_data.get('products_count', 10)
        try:
            products_count = int(products_count)
        except Exception as e:
            return {'error': str(e)}
        products_count = min(max(products_count, 1), 50)

        json = parce_product_task(products_count)
        
        return {'input': {'products_count': products_count},
                'output':[json]}

    def to_representation(self, instance):
        # Получаем метод HTTP-запроса
        method = self.context['request'].method
        
        if method == 'POST':
            # Возвращаем значение products_count при POST-запросе
            return instance
        else:
            # Возвращаем список продуктов при других запросах
            return {
                'name': instance.name,
                'price': instance.price,
                'description': instance.description,
                'image_url': instance.image_url,
                'discount': instance.discount
            }
