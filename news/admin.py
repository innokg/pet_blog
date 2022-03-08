from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import News, Category


class NewsAdminForm(forms.ModelForm): #создаем специальный класс, который связывает с моделью News для Ckeditor
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'



class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm #используем класс NewsAdmin для подключения
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published',
                    'views', 'get_image' ) #поле, которое показывает что мы увидем в админке
    list_display_links = ('id', 'title') # ссылки в админке
    search_fields = ('title', 'content') # появляется поле для поиска по параметрам
    list_editable = ('is_published',) # показывает в админке какие поля мы можем корректировать
    list_filter = ('is_published', 'category') # фильтрация
    fields = ('title', 'category', 'content', 'image', 'get_image', 'is_published', 'views',
              'created_at', 'updated_at')
    readonly_fields = ('get_image', 'views',
              'created_at', 'updated_at')

    def get_image(self, obj): #возвращает HTML код картинки
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75" >')
        else:
            return 'Нет фото'

    get_image.short_description = 'Миниатюра'  #типа verbose_name для админки

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title') #поле, которое показывает что мы увидем в админке
    list_display_links = ('id', 'title') # ссылки в админке
    search_fields = ('title',) # появляется поле для поиска по параметрам

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

