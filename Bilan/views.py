from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from Charge.models import Charge
from Epargne.models import Epargne
from Revenu.models import Revenu


class BilanFinancierView(LoginRequiredMixin, TemplateView):
    template_name = "Bilan/bilan_financier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Proportions de base pour chaque catégorie
        proportion_base_fixes = 50  # Exemple : 60% pour les charges fixes
        proportion_base_plaisir = 30  # Exemple : 20% pour les charges plaisir
        proportion_base_investissement = 10  # Exemple : 10% pour les investissements
        proportion_base_epargne = 10  # Exemple : 10% pour l'épargne

        # Calcul des montants totaux par catégorie
        charges_fixes = Charge.objects.filter(category="Fixes", user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        charges_plaisir = Charge.objects.filter(category="Variables", user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        investissement = Epargne.objects.filter(category="Investissements", user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        epargne = Epargne.objects.filter(category="Mensuels", user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0

        # Total des revenus
        total_revenu = Revenu.objects.filter(user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0

        # Calcul des proportions réelles
        total_charges = charges_fixes + charges_plaisir + investissement + epargne
        proportion_fixes = (charges_fixes / total_revenu * 100) if total_revenu > 0 else 0
        proportion_plaisir = (charges_plaisir / total_revenu * 100) if total_revenu > 0 else 0
        proportion_investissement = (investissement / total_revenu * 100) if total_revenu > 0 else 0
        proportion_epargne = (epargne / total_revenu * 100) if total_revenu > 0 else 0


        # Comparaisons avec les proportions de base
        fixe_vrai = proportion_fixes >= proportion_base_fixes
        plaisir_vrai = proportion_plaisir >= proportion_base_plaisir
        investissement_vrai = proportion_investissement >= proportion_base_investissement
        epargne_vrai = proportion_epargne >= proportion_base_epargne

        # Calcul du reste à vivre (RAV)
        reste_a_vivre = total_revenu - total_charges
        proportion_rav = (reste_a_vivre / total_revenu * 100) if total_revenu > 0 else 0

        # Vérifier si le bilan est positif ou négatif
        positif = reste_a_vivre > 0
        negatif = reste_a_vivre < 0

        # Ajouter les valeurs calculées au contexte
        context.update({
            'charges_fixes': charges_fixes,
            'charges_plaisir': charges_plaisir,
            'investissement': investissement,
            'epargne': epargne,
            'proportion_fixes': round(proportion_fixes, 2),
            'proportion_plaisir': round(proportion_plaisir),
            'proportion_investissement': round(proportion_investissement),
            'proportion_epargne': round(proportion_epargne),
            'proportion_base_fixes': proportion_base_fixes,
            'proportion_base_plaisir': proportion_base_plaisir,
            'proportion_base_investissement': proportion_base_investissement,
            'proportion_base_epargne': proportion_base_epargne,
            'fixe_vrai': fixe_vrai,
            'plaisir_vrai': plaisir_vrai,
            'investissement_vrai': investissement_vrai,
            'epargne_vrai': epargne_vrai,
            'reste_a_vivre': reste_a_vivre,
            'positif': positif,
            'negatif': negatif,
            "proportion_rav": round(proportion_rav, 2),
        })

        return context