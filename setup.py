# typical compilation (perhaps as root or sudo, see README.txt):
# python setup.py build
# python setup.py install

# To build in current working directory:
# python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

from numpy import get_include
numpy_include_dir = get_include()

ext_modules = [Extension("pykseq", ["./pykseq/pykseq.pyx"], libraries=["z"],
                         include_dirs=['./pykseq'],
                         library_dirs=['./pykseq']),
               Extension("_emirge", ["_emirge.pyx"],
                         include_dirs=[numpy_include_dir],
                         extra_compile_args=["-O3"]),
               Extension("_emirge_amplicon", ["_emirge_amplicon.pyx"],
                         include_dirs=[numpy_include_dir, './pykseq'],
                         libraries=["z"], library_dirs = ['./pykseq'],
                         extra_compile_args=["-O3"])]

setup(
    name = 'EMIRGE',
    description = 'EMIRGE reconstructs full length sequences from short sequencing reads',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,

    scripts = ["emirge.py",
               "emirge_amplicon.py",
               "emirge_rename_fasta.py"],

    author="Christopher Miller",
    author_email="christopher.s.miller@ucdenver.edu",
    version="0.5.0",
    license="GPLv3",
)

print ""
print "NOTE:"
print "To download a standard candidate SSU database to use with EMIRGE, run the script"
print "python emirge_download_candidate_db.py"
