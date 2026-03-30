import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
data = pd.DataFrame({
    'Rain': ['No','No','Yes','Yes', 'No', 'Yes', 'Yes', 'No'],
    'Traffic': ['Yes','No','Yes','No','Yes','Yes','No','No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No','No','Yes','Yes', 'No']
})
for col in data.columns:
    data[col] = data[col].astype('category')
model = DiscreteBayesianNetwork([
    ('Rain', 'Traffic'),
    ('Traffic', 'ArriveLate')
])
model.fit(data)
inference = VariableElimination(model)
result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})
print(result)
