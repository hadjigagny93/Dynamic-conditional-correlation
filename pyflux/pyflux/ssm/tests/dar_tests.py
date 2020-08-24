import numpy as np
import pyflux as pf

noise = np.random.normal(0,1,100)
data = np.zeros(100)

for i in range(1,len(data)):
	data[i] = 0.9*data[i-1] + noise[i]

def test_couple_terms():
	"""
	Tests an DAR model with 1 AR and that
	the latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1)
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_couple_terms_integ():
	"""
	Tests an DAR model with 1 AR, integrated once, and that
	the latent variable list length is correct, and that the estimated
	latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1, integ=1)
	x = model.fit()
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_bbvi():
	"""
	Tests an DAR model estimated with BBVI and that the length of the latent variable
	list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1)
	x = model.fit('BBVI',iterations=100)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_mh():
	"""
	Tests an DAR model estimated with Metropolis-Hastings and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1)
	x = model.fit('M-H',nsims=300)
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_laplace():
	"""
	Tests an DAR model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1)
	x = model.fit('Laplace')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_pml():
	"""
	Tests a PML model estimated with Laplace approximation and that the length of the 
	latent variable list is correct, and that the estimated latent variables are not nan
	"""
	model = pf.DAR(data=data, ar=1)
	x = model.fit('PML')
	assert(len(model.latent_variables.z_list) == 3)
	lvs = np.array([i.value for i in model.latent_variables.z_list])
	assert(len(lvs[np.isnan(lvs)]) == 0)

def test_predict_length():
	"""
	Tests that the prediction dataframe length is equal to the number of steps h
	"""
	model = pf.DAR(data=data, ar=2)
	x = model.fit()
	x.summary()
	assert(model.predict(h=5).shape[0] == 5)

def test_predict_is_length():
	"""
	Tests that the prediction IS dataframe length is equal to the number of steps h
	"""
	model = pf.DAR(data=data, ar=2)
	x = model.fit()
	assert(model.predict_is(h=5).shape[0] == 5)

def test_predict_nans():
	"""
	Tests that the predictions are not nans
	"""
	model = pf.DAR(data=data, ar=2)
	x = model.fit()
	x.summary()
	assert(len(model.predict(h=5).values[np.isnan(model.predict(h=5).values)]) == 0)

def test_predict_is_nans():
	"""
	Tests that the in-sample predictions are not nans
	"""
	model = pf.DAR(data=data, ar=2)
	x = model.fit()
	x.summary()
	assert(len(model.predict_is(h=5).values[np.isnan(model.predict_is(h=5).values)]) == 0)