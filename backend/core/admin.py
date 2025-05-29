from django.contrib import admin
from .models import (
    Osoba, Doktorant, Doktorat, KomisjaDr, RD, Recenzent,
    Historia, SzablonZdarzenia, SzablonDokumentu, DokumentWniosekUchwala,
    Uprawnienia, User
)

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'tytulStopien')
    search_fields = ('imie', 'nazwisko', 'email')
    ordering = ('nazwisko',)

@admin.register(Doktorant)
class DoktorantAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'adres_miasto')
    search_fields = ('imie', 'nazwisko', 'email')
    ordering = ('nazwisko',)

@admin.register(Doktorat)
class DoktoratAdmin(admin.ModelAdmin):
    list_display = ('doktorant', 'tytul', 'promotor', 'RD')
    search_fields = ('tytul',)
    ordering = ('doktorant',)

@admin.register(KomisjaDr)
class KomisjaDrAdmin(admin.ModelAdmin):
    list_display = ('doktorat', 'osoba', 'funkcja', 'data_powolania')
    ordering = ('doktorat',)

@admin.register(RD)
class RDAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'wydzial', 'email')

@admin.register(Recenzent)
class RecenzentAdmin(admin.ModelAdmin):
    list_display = ('osoba', 'doktorat', 'czy_aktywny', 'czy_wyroznienie')

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('doktorat', 'data_zdarzenia', 'szablon')
    ordering = ('-data_zdarzenia',)

@admin.register(SzablonZdarzenia)
class SzablonZdarzeniaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'czy_aktywny')

@admin.register(SzablonDokumentu)
class SzablonDokumentuAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'typ', 'czy_aktywny')

@admin.register(DokumentWniosekUchwala)
class DokumentAdmin(admin.ModelAdmin):
    list_display = ('doktorat', 'numer', 'data_utworzenia')

@admin.register(Uprawnienia)
class UprawnieniaAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'rola')
    search_fields = ('imie', 'nazwisko', 'email')
