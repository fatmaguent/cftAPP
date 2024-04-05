from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)

    class Meta:
        # Supprimer la ligne ordering si vous n'avez pas besoin de trier par le champ created
        ordering = ['nom']  # Par exemple, trier par le champ nom
