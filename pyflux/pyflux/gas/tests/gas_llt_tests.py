import numpy as np
import pyflux as pf

noise = np.random.normal(0,1,200)
data = np.zeros(200)

for i in range(1,len(data)):
	data[i] = 1.0*data[i-1] + noise[i]

countdata = np.random.poisson(3,200)

def test_couple_terms():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_couple_terms_integ():
	"""
	Tests  latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, integ=1, family=pf.GASNormal())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_bbvi():
	"""
	Tests an GAS model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_mh():
	"""
	Tests an GAS model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace():
	"""
	Tests an GAS model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)

def test_predict_nans():
	"""
	Tests that the predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)

def test_predict_is_nans():
	"""
	Tests that the in-sample predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASNormal())
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)



def test_t_couple_terms():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_couple_terms_integ():
	"""
	Tests an GAS model with 1 AR and 1 MA term, integrated once, and that
	the latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, integ=1, family=pf.GASt())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_bbvi():
	"""
	Tests an GAS model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_mh():
	"""
	Tests an GAS model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_laplace():
	"""
	Tests an GAS model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_t_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_t_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)

def test_t_predict_nans():
	"""
	Tests that the predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)

def test_t_predict_is_nans():
	"""
	Tests that the in-sample predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASt())
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)



def test_skewt_couple_terms():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 5)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_skewt_couple_terms_integ():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, integ=1, family=pf.GASSkewt())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 5)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_skewt_bbvi():
	"""
	Tests an GAS model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 5)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_skewt_mh():
	"""
	Tests an GAS model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 5)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

""" Uncomment in future if Skewt becomes more robust
def test_skewt_laplace():
	Tests an GAS model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 4)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)
"""

def test_skewt_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 5)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_skewt_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_skewt_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)


def test_skewt_predict_nans():
	"""
	Tests that the predictions are not nans
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	"""
	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)
"""

def test_skewt_predict_is_nans():

	Tests that the in-sample predictions are not nans

	model = pf.GASLLT(data=data, family=pf.GASSkewt())
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)
"""
def test_laplace_couple_terms():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_couple_terms_integ():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=data, integ=1, family=pf.GASLaplace())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_bbvi():
	"""
	Tests an GAS model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_mh():
	"""
	Tests an GAS model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_laplace():
	"""
	Tests an GAS model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_laplace_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)

def test_laplace_predict_nans():
	"""
	Tests that the predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)

def test_laplace_predict_is_nans():
	"""
	Tests that the in-sample predictions are not nans
	"""
	model = pf.GASLLT(data=data, family=pf.GASLaplace())
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)


def test_poisson_couple_terms():
	"""
	Tests latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 2)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_poisson_bbvi():
	"""
	Tests an GAS model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 2)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_poisson_mh():
	"""
	Tests an GAS model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 2)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_poisson_laplace():
	"""
	Tests an GAS model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 2)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_poisson_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 2)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_poisson_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_poisson_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)

def test_poisson_predict_nans():
	"""
	Tests that the predictions are not nans
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)

def test_poisson_predict_is_nans():
	"""
	Tests that the in-sample predictions are not nans
	"""
	model = pf.GASLLT(data=countdata, family=pf.GASPoisson())
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)