from django.contrib import admin
from django.utils.html import format_html
from .models import Episode, Testimonial, Book, Event, Partner

class BaseImageAdmin(admin.ModelAdmin):
    #readonly_fields = ('image_preview',) - passed by the subclasses

    def image_preview(self, obj, field_name):
        if getattr(obj, field_name):
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;"/>', getattr(obj, field_name).url)
        return "No Image"
    
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }

@admin.register(Episode)
class EpisodeAdmin(BaseImageAdmin):
    list_display = ('title', 'guest_name', 'pub_date', 'image_preview_column')
    list_filter = ['pub_date', 'created_at']
    search_fields = ('title', 'guest_name', 'description')
    list_filter = ('pub_date',)
    readonly_fields = ('created_at', 'updated_at', 'image_preview_column')

    fieldsets = (
        ('Episode Details', {
            'fields': ('title', 'summarized_title', 'guest_name', 'link'
                )}),
        ('Content', {
            'fields': ('description',)}),
        ('Media', {
            'fields': ('img', 'image_preview_column')}),
        ('Dates', {
            'fields': ('pub_date', 'created_at', 'updated_at')}),
    )

    def image_preview_column(self, obj):
        return self.image_preview(obj, 'img')
    image_preview_column.short_description = 'Image Preview'

@admin.register(Testimonial)
class TestimonialAdmin(BaseImageAdmin):
    list_display = ('name', 'country', 'testimony_date', 'image_preview_column')
    list_filter = ['testimony_date', 'created_at', 'country']
    search_fields = ('name', 'country', 'testimony')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_column')

    fieldsets = (
        ('Testimonial Details', {
            'fields': ('name', 'country', 'testimony_date')}),
        ('Testimonial', {
            'fields': ('testimony',)}),
        ('Media', {
            'fields': ('img', 'image_preview_column')}),
        ('Dates', {
            'fields': ('created_at', 'updated_at')}),
    )

    def image_preview_column(self, obj):
        return self.image_preview(obj, 'img')
    image_preview_column.short_description = 'Image Preview'

@admin.register(Book)
class BookAdmin(BaseImageAdmin):
    list_display = ('title', 'author', 'image_preview_column')
    list_filter = ['created_at']
    search_fields = ('title', 'author', 'description')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_column')

    fieldsets = (
        ('Book Details', {
            'fields': ('title', 'author', 'price')}),
        ('Content', {
            'fields': ('description', 'summary')}),
        ('Media', {
            'fields': ('img', 'image_preview_column')}),
        ('Dates', {
            'fields': ('created_at', 'updated_at')}),
    )  

    def image_preview_column(self, obj):
        return self.image_preview(obj, 'img')
    image_preview_column.short_description = 'Cover Preview' 

@admin.register(Event)
class EventAdmin(BaseImageAdmin):
    list_display = ('title', 'host', 'price', 'event_date', 'location', 'image_preview_column')
    list_filter = ['event_date', 'created_at', 'location', 'price']
    search_fields = ('title', 'location', 'description', 'host', 'summary')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_column')

    fieldsets = (
        ('Event Details', {
            'fields': ('title', 'host', 'location')}),
        ('Content', {
            'fields': ('description', 'summary')}),
        ('Media', {
            'fields': ('img', 'image_preview_column')}),
        ('Dates', {
            'fields': ('event_date', 'created_at', 'updated_at')}),
    )

    def image_preview_column(self, obj):
        return self.image_preview(obj, 'img')
    image_preview_column.short_description = 'Image Preview'

@admin.register(Partner)
class PartnerAdmin(BaseImageAdmin):
    list_display = ('name', 'website', 'image_preview_column')
    list_filter = ['created_at']
    search_fields = ('name', 'website')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_column')

    fieldsets = (
        ('Partner Details', {
            'fields': ('name', 'website')}),
        ('Media', {
            'fields': ('img', 'image_preview_column')}),
        ('Dates', {
            'fields': ('created_at', 'updated_at')}),
    )

    def image_preview_column(self, obj):
        return self.image_preview(obj, 'img')
    image_preview_column.short_description = 'Logo Preview'


admin.site.site_header = 'Hope Against Hope Show Admin'
admin.site.site_title = 'Hope Against Hope Show' 
admin.site.index_title = 'Welcome to Hope Against Hope Show Admin Dashboard'

