from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
model = DiscreteBayesianNetwork([
    ('Income', 'Default'),
    ('Credit', 'Default')
])
cpd_income = TabularCPD(
    variable='Income',
    variable_card=2,
    values=[[0.6], [0.4]]
)
cpd_credit = TabularCPD(
    variable='Credit',
    variable_card=2,
    values=[[0.7], [0.3]]
)
cpd_default = TabularCPD(
    variable='Default',
    variable_card=2,
    values=[
        [0.95, 0.8, 0.9, 0.5],   
        [0.05, 0.2, 0.1, 0.5]    
    ],
    evidence=['Income', 'Credit'],
    evidence_card=[2, 2]
)
model.add_cpds(cpd_income, cpd_credit, cpd_default)
model.check_model()
infer = VariableElimination(model)
result = infer.query(variables=['Default'], evidence={'Income': 1, 'Credit': 0})
print(result)
