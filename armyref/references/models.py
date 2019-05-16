from django.db import models
from ordered_model.models import OrderedModel


class Reference(OrderedModel):
    START_SUB_PHASE = 0
    DURING_SUB_PHASE = 1
    END_SUB_PHASE = 2
    SUB_PHASES = (
        (START_SUB_PHASE, 'Start'),
        (DURING_SUB_PHASE, 'During'),
        (END_SUB_PHASE, 'End'),
    )

    name = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    phase = models.ForeignKey('armies.Phase', on_delete=models.CASCADE)
    sub_phase = models.IntegerField(choices=SUB_PHASES, default=DURING_SUB_PHASE)

    order_with_respect_to = ('phase', 'sub_phase')

    class Meta:
        ordering = ['phase', 'sub_phase']

    def __str__(self):
        return self.name

    @property
    def non_default_sub_phase(self):
        return self.sub_phase != self.DURING_SUB_PHASE
