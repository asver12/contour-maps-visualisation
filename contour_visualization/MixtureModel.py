from contour_visualization import Gaussian, helper
from sklearn.mixture import GaussianMixture
from sklearn import preprocessing
import pandas as pd

import logging

logger = logging.getLogger(__name__)


class MixtureModel:
    def __init__(self, data, normalize=True, n_components=3, covariance_type="full", max_iter=20, random_state=0, *args,
                 **kwargs):
        if normalize:
            x = data.values  # returns a numpy array
            min_max_scaler = preprocessing.MinMaxScaler()
            x_scaled = min_max_scaler.fit_transform(x)
            data = pd.DataFrame(x_scaled)
        self.data = data
        self.n_components = n_components
        self.estimator = GaussianMixture(n_components=n_components, covariance_type=covariance_type, max_iter=max_iter,
                                         random_state=random_state, *args, **kwargs)
        self.estimator.fit(data)

    def learn_new(self, n_components, covariance_type, max_iter=20, random_state=0, *args, **kwargs):
        self.n_components = n_components
        self.estimator = GaussianMixture(n_components=n_components, covariance_type=covariance_type, max_iter=max_iter,
                                         random_state=random_state, *args, **kwargs)
        self.estimator.fit(self.data)

    def get_gaussians(self):
        dataset = []
        for n in range(self.n_components):
            means = self.estimator.means_[n, :2]
            cov_matrix = self.estimator.covariances_[n][:2, :2]
            weight = self.estimator.weights_[n]
            logging.info("Means[{}]: {}".format(n, means))
            logging.info("Cov-Matrix[{}]: {}".format(n, cov_matrix))
            logging.info("weights[{}]: {}".format(n, weight))
            dataset.append(
                Gaussian.Gaussian(weight=weight, means=means, cov_matrix=cov_matrix))
        return dataset
