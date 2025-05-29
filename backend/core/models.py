from django.db import models

class Osoba(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    tytulStopien = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    stanowisko = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    link_do_profilu_gov = models.URLField(blank=True, null=True)
    specjalnosci = models.TextField(blank=True, null=True)
    plec = models.CharField(max_length=1)
    tytul_po = models.CharField(max_length=255, blank=True, null=True)
    imie_nazwisko_dopelniacz = models.CharField(max_length=255)
    imie_nazwisko_celownik = models.CharField(max_length=255)
    imie_nazwisko_biernik = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tytulStopien or ''} {self.imie} {self.nazwisko}"

class Doktorant(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    email = models.EmailField()
    tytulStopien = models.CharField(max_length=255)
    adres_miasto = models.CharField(max_length=255)
    adres_kod_pocztowy = models.CharField(max_length=20)
    adres_ulica = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    imie_nazwisko_celownik = models.CharField(max_length=255)
    imie_nazwisko_biernik = models.CharField(max_length=255)
    imie_nazwisko_dopelniacz = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tytulStopien} {self.imie} {self.nazwisko}"

class Doktorat(models.Model):
    RD = models.ForeignKey('core.RD', on_delete=models.SET_NULL, null=True, blank=True)
    doktorant = models.ForeignKey('core.Doktorant', on_delete=models.CASCADE)
    tytul = models.CharField(max_length=255, blank=True, null=True)
    promotor = models.ForeignKey('core.Osoba', on_delete=models.CASCADE, related_name='promotor_doktoraty')
    promotorPomocniczy = models.ForeignKey(
        'core.Osoba', on_delete=models.CASCADE,
        related_name='promotor_pomocniczy_doktoraty',
        blank=True, null=True
    )
    kopromotor = models.ForeignKey(
        'core.Osoba', on_delete=models.CASCADE,
        related_name='kopromotor_doktoraty',
        blank=True, null=True
    )
    rozprawa = models.FileField(upload_to='rozprawy/', blank=True, null=True)
    komentarz = models.CharField(max_length=255, blank=True, null=True)
    komisjaDr = models.ManyToManyField('core.Osoba', through='core.KomisjaDr')

    def __str__(self):
        return f"{self.tytul or 'Doktorat'} – {self.doktorant}"

class KomisjaDr(models.Model):
    doktorat = models.ForeignKey('core.Doktorat', on_delete=models.CASCADE)
    osoba = models.ForeignKey('core.Osoba', on_delete=models.CASCADE)
    funkcja = models.CharField(max_length=255)
    data_powolania = models.DateField()
    data_odwolania = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.funkcja} – {self.osoba} (doktorat ID: {self.doktorat.id})"

class RD(models.Model):
    nazwa = models.CharField(max_length=255)
    wydzial = models.CharField(max_length=255)
    adres = models.TextField(blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to='logotypy_RD/', blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Recenzent(models.Model):
    osoba = models.ForeignKey('core.Osoba', on_delete=models.CASCADE)
    doktorat = models.ForeignKey('core.Doktorat', on_delete=models.CASCADE)
    czy_aktywny = models.BooleanField(default=True)
    czy_wyroznienie = models.BooleanField(default=False)
    data_powolania = models.DateField(blank=True, null=True)
    data_recenzji = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.osoba} – recenzent doktoratu {self.doktorat_id}"

class SzablonZdarzenia(models.Model):
    nazwa = models.CharField(max_length=255)
    opis = models.TextField(blank=True, null=True)
    czy_aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa

class Historia(models.Model):
    doktorat = models.ForeignKey('core.Doktorat', on_delete=models.CASCADE)
    data_zdarzenia = models.DateField()
    opis = models.TextField(blank=True, null=True)
    szablon = models.ForeignKey('core.SzablonZdarzenia', on_delete=models.SET_NULL, blank=True, null=True)
    utworzono_przez = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.doktorat} – {self.szablon or 'Zdarzenie'} – {self.data_zdarzenia}"

class SzablonDokumentu(models.Model):
    nazwa = models.CharField(max_length=255)
    typ = models.CharField(max_length=255)
    tresc = models.TextField()
    czy_aktywny = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.typ}: {self.nazwa}"

class DokumentWniosekUchwala(models.Model):
    doktorat = models.ForeignKey('core.Doktorat', on_delete=models.CASCADE)
    szablon = models.ForeignKey('core.SzablonDokumentu', on_delete=models.CASCADE)
    plik = models.FileField(upload_to='dokumenty/')
    numer = models.CharField(max_length=50)
    data_utworzenia = models.DateField(auto_now_add=True)
    utworzony_przez = models.CharField(max_length=255)

    def __str__(self):
        return f"Dokument {self.numer} ({self.doktorat})"

class Uprawnienia(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class User(models.Model):
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    haslo = models.CharField(max_length=255)
    rola = models.ForeignKey('core.Uprawnienia', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.rola})"
