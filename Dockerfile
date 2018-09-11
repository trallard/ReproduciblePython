FROM jupyter/minimal-notebook:latest

LABEL maintainer="Tania Allard <tania.allard@hellosoda.com>"

USER $NB_UID

# Install Python 3 packages
RUN pip install hypothesis nbval nbdime recipy pipenv datapackage
RUN conda install --quiet --yes \ 
    'pandas=0.23*' \
    'matplotlib=2.2*' \
    'scipy=1.1*' \
    'pytest' \
    'cookiecutter' \    
    'seaborn=0.9*' && \
    npm cache clean --force && \
    rm -rf $CONDA_DIR/share/jupyter/lab/staging && \
    rm -rf /home/$NB_USER/.cache/yarn && \
    rm -rf /home/$NB_USER/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions /home/$NB_USER

USER $NB_UID