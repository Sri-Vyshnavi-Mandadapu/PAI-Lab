from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
model = DiscreteBayesianNetwork([
    ('Signal', 'Failure'),
    ('Hardware', 'Failure')
])
cpd_signal = TabularCPD(
    variable='Signal',
    variable_card=2,
    values=[[0.7], [0.3]]
)
cpd_hardware = TabularCPD(
    variable='Hardware',
    variable_card=2,
    values=[[0.8], [0.2]]
)
cpd_failure = TabularCPD(
    variable='Failure',
    variable_card=2,
    values=[
        [0.95, 0.6, 0.7, 0.2],   
        [0.05, 0.4, 0.3, 0.8]    
    ],
    evidence=['Signal', 'Hardware'],
    evidence_card=[2, 2]
)
model.add_cpds(cpd_signal, cpd_hardware, cpd_failure)
model.check_model()
infer = VariableElimination(model)
result = infer.query(variables=['Failure'], evidence={'Signal': 1, 'Hardware': 1})
print(result)
