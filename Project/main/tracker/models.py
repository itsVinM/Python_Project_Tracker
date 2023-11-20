from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProjectTracker(models.Model):
    #STATUS CHOICES

    COMPLETED="COMPLETED"
    NOT_STARTED="NOT STARTED"
    CANCELED="CANCELED"
    zero="STARTED"
    one="ON TIME"
    two="SLIGHT DELAY"
    STATUS_CHOICES=[
        (COMPLETED, 'COMPLETED'), 
        (NOT_STARTED, 'NOT STARTED'), 
        (CANCELED, 'CANCELED'), 
        (zero, 'STARTED'), 
        (one, 'ON TIME'), 
        (two, 'SLIGHT DELAY')
    ]

    #LAB CHOICE
    ALL_LABS="All"
    PML="PML"
    RML="RML"
    SPL="SPL"
    TBA="TBA"
    LAB_CHOICES=[
        (ALL_LABS, "All"), 
        (PML, "PML"), 
        (RML, "RML"),
        (SPL, "SPL"), 
        (TBA, "TBA")
    ]
    

    # MAG CHOICES
    
    QL_Goal="QL Goal"
    R73_AUTOMOS="R73 Auto/R1 MOS"
    RE1_POWERMOS="RE1 PowerMos"
    RE2_GAN="RE2-GAN"

    MAG_CHOICES=[
            (QL_Goal, 'QL Goal'),
            (RE2_GAN, 'RE2 GAN'),
            (R73_AUTOMOS, 'R73 Auto/R1 MOS'),
            (RE1_POWERMOS, 'RE1 PowerMos')
    ]

    Sgate="S Gate"
    Agate="A Gate"
    Vgate="V Gate"
    Rgate="R Gate"
    NEXTGATE_CHOICES=[
        (Sgate, "S Gate"),
        (Agate, "A Gate"), 
        (Vgate, "V Gate"), 
        (Rgate, "R Gate")
    ]

    projectId= models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= NOT_STARTED)
    leader = models.ForeignKey(User, null=True,blank=True,on_delete=models.SET_NULL)
    lab=models.CharField(max_length=50, choices=LAB_CHOICES,null=True,blank=True)
    mag=models.CharField(max_length=50,choices=MAG_CHOICES,null=True,blank=True)

    # Main dates
    sgate_date=models.DateField(null=True, blank=True)
    agate_date=models.DateField(null=True, blank=True)
    vgate_date=models.DateField(null=True, blank=True)
    rgate_date=models.DateField(null=True,blank=True)

    actual_sgate_date=models.DateField(null=True, blank=True)
    actual_agate_date=models.DateField(null=True, blank=True)
    actual_vgate_date=models.DateField(null=True, blank=True)
    actual_rgate_date = models.DateField(null=True,blank=True)

    
    nextgate=models.CharField(max_length=50, choices=NEXTGATE_CHOICES,null=True,blank=True,default= Sgate)
    nextgate_date=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.name

    @property
    def week_delay(self):
        if self.actual_rgate_date is None or self.rgate_date is None or self.sgate_date is None:
            return None

        delay = ((self.actual_rgate_date - self.sgate_date).days-(self.rgate_date - self.sgate_date).days)/7
        total_time= ((self.rgate_date-self.sgate_date).days)/7
        week_delay =(delay/ total_time)*100 

        #return f"{week_delay:.2f}%"
        return round(week_delay, 2)
    
    GaN="GaN Program"
    All_Projects="Project"
    LEVEL_CHOICES=[(GaN,"GaN Program"), (All_Projects, "Project")]

    measurement_method=models.CharField(max_length=250, null=True, blank=True)
    reason=models.CharField(max_length=50,null=True,blank=True)
    purpose=models.TextField(null=True, blank=True)
    comment=models.TextField(null=True, blank=True)
    level=models.CharField(max_length=50,choices=LEVEL_CHOICES, null=True, blank=True)                    #add choices
    CapEx_Ref=models.CharField(max_length=250, null=True, blank=True)  

    support=models.CharField(max_length=100, null=True, blank=True)
    testEng=models.CharField(max_length=100, null=True, blank=True)
    qualityEng=models.CharField(max_length=100, null=True, blank=True)
    lastUpdate=models.DateField(null=True, blank=True)
    currentForecast=models.DateField(null=True, blank=True)
    #Other gates


