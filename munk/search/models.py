from django.db import models
from django.forms import ModelForm

class SearchParameters(models.Model):
# Know/Unknown Peptide Search Parameters. Fields required?
# RT Range
    rt_rangestart = models.DecimalField(max_digits=20, decimal_places=10)
    rt_rangestop =  models.DecimalField(max_digits=20, decimal_places=10)
# Precursor Ion M/Z Range. fields required?
    precursor_rangestart = models.IntegerField(default=100)
    precursor_ionstop = models.IntegerField(default=1000)
# LCMS Inversion Parameter:
# M/Z equivalence Windows, in PPM
    mz_equivalence_window = models.IntegerField(help_text='in PPM', default=50)
# XIC Peak Signal/Noise Parameter:
# Characteristic Chromatographic Peak Width
    min_peakwidth = models.DecimalField(max_digits=20, decimal_places=4)
# Filter MS-Only Search Range
    filter_ms_only = models.BooleanField()
# FileField
    rawfile = models.FileField(upload_to='raw_files/')

    def __unicode__(self):
        return '%s' % self.pk

    # create form class
class MunkSearchForm(ModelForm):
    class Meta:
        model = SearchParameters

class ParentIonTable(models.Model):
# Parent Ion #
    parent_ion = models.IntegerField()
# Scan #
    scan_number = models.IntegerField()
# M/Z
    mz_result = models.DecimalField(max_digits=20, decimal_places=10)
# +-dmz
    dmz_diff = models.DecimalField(max_digits=8, decimal_places=7)
# RT(min)
    min_rt = models.DecimalField(max_digits=8, decimal_places=7)
#Best Pep. Seq
#    best_pep_seq = models.DecimalField(max_digits=8, decimal_places=7, blank=true)
# Best XCorr Score
#    best_xcorr = models.DecimalField(max_digits=8, decimal_places=7)
# Area
    area_amt = models.DecimalField(max_digits=9, decimal_places=2)
# Area Percentile
    area_pect = models.DecimalField(max_digits=6, decimal_places=2)
