from setuptools import setup
import os
import glob

here = os.path.abspath(os.path.dirname(__file__))
desc = 'A software that can be used to build surrogates'
keywords = 'hyperparameter optimization empirical evaluation surrogate benchmark'

package_dir = {
    'Surrogates':
    'Surrogates',
    'Surrogates.DataExtraction':
    'Surrogates/DataExtraction',
    'Surrogates.RegressionModels':
    'Surrogates/RegressionModels',
    'Surrogates.RegressionModels.GaussianProcess_src':
    'Surrogates/RegressionModels/GaussianProcess_src',
    'Surrogates.RegressionModels.GaussianProcess_src.spearmint':
    'Surrogates/RegressionModels/GaussianProcess_src/spearmint'
}
#'Surrogates.RegressionModels.RandomForests':
# 'Surrogates/RegressionModels/RandomForests',
#'Surrogates.RegressionModels.RandomForests.pyfastrf':
# 'Surrogates/RegressionModels/RandomForests/pyfastrf'
#}

#conditional_gp = glob.glob(os.path.join(here, 'Surrogates/RegressionModels/'
#                                              'conditional_gp/*.py'))
#conditional_gp_spearmint = glob.glob(os.path.join(here,
#                                                  'Surrogates/RegressionModels/'
#                                                  'conditional_gp/*/*.py'))

#spearmint_gp = glob.glob(os.path.join(here, 'Surrogates/RegressionModels/'
#                                            'spearmint_gp/*.py'))
#spearmint_gp_OptSizeChooser = \
#    glob.glob(os.path.join(here, 'Surrogates/RegressionModels/spearmint_gp/'
#                                 'OptSizeChooser/*.py'))
#spearmint_gp_OptSizeChooser_spearmint = \
#    glob.glob(os.path.join(here, 'Surrogates/RegressionModels/spearmint_gp/'
#                                 'OptSizeChooser/spearmint/*.py'))

#RandomForests_pyfastrf_fastrf_lib = \
#    glob.glob(os.path.join(here, 'Surrogates/RegressionModels/RandomForests/'
#                                 'pyfastrf/fastrf/lib/*.jar'))

#data_files = [('Surrogates/RegressionModels/conditional_gp', conditional_gp),
#              ('Surrogates/RegressionModels/conditional_gp/spearmint',
#               conditional_gp_spearmint),
#              ('Surrogates/RegressionModels/spearmint_gp/', spearmint_gp),
#              ('Surrogates/RegressionModels/spearmint_gp/OptSizeChooser/',
#               spearmint_gp_OptSizeChooser),
#              ('Surrogates/RegressionModels/spearmint_gp/OptSizeChooser/'
#               'spearmint/', spearmint_gp_OptSizeChooser_spearmint),
#              ('Surrogates/RegressionModels/RandomForests/pyfastrf/fastrf/lib',
#               RandomForests_pyfastrf_fastrf_lib)
#              ]

#package_data = {'Surrogates.RegressionModels':
#                glob.glob(os.path.join(here, 'Surrogates/RegressionModels/'
#                                             'conditional_gp/*.py')),
#                'Surrogates.RegressionModels':
#                glob.glob(os.path.join(here, 'Surrogates/RegressionModels/'
#                                             'conditional_gp/*/*.py'))
#                }

scripts = [
    'scripts/regression_performance.py', 'scripts/make_data',
    'scripts/regression_performance_looo.py', 'scripts/extract.py',
    'scripts/trainer.py', 'scripts/daemon_benchmark.py',
    'scripts/daemonize_benchmark.py', 'scripts/daemon_whisperer.py'
]


def get_find_packages():
    packages = [
        'Surrogates', 'Surrogates.DataExtraction',
        'Surrogates.RegressionModels',
        'Surrogates.RegressionModels.GaussianProcess_src',
        'Surrogates.RegressionModels.GaussianProcess_src.spearmint'
    ]
    #'Surrogates.RegressionModels.RandomForests',
    #'Surrogates.RegressionModels.RandomForests.pyfastrf'

    return packages


setup(
    name='Surrogates',
    version='0.1',
    url='Nan',
    license='LGPLv3',
    platforms=['Linux'],
    author='Katharina Eggensperger',
    python_requires='==3.8',
    install_requires=[
        'argparse', 'networkx==2.5', 'nose==1.3.7', 'numpy==1.19.4',
        'pylint==2.6.0', 'pyparsing==2.4.7', 'python-daemon==2.2.4',
        'scikit-learn==0.23.2', 'scipy==1.5.4'
    ],
    author_email='eggenspk@informatik.uni-freiburg.de',
    description=desc,
    long_description="NONE",
    keywords=keywords,
    packages=get_find_packages(),
    package_dir=package_dir,
    #    data_files=data_files,
    test_suite="tests.testsuite.suite",
    scripts=scripts,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ])
