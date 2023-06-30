import os
import pandas as pd
import plotly.graph_objects as go
import numpy as np

folders = ['0.5', '0.6', '0.7', '0.8', '0.9']

class LossSurface():
    def addLossSurfaceTraces(self, prediction_surface_figure, path):

        for folder in folders:
            data_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'data_surface.csv'))
            data_surface = data_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=data_surface.values.tolist(),
                                                           x=np.array(data_surface.columns),
                                                           y=np.array(data_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'data'))

            # pinn
            pinn_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'pinn_surface.csv'))
            pinn_surface = pinn_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=pinn_surface.values.tolist(),
                                                           x=np.array(pinn_surface.columns),
                                                           y=np.array(pinn_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'pinn'))

            # bc
            bc_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'bc_surface.csv'))
            bc_surface = bc_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=bc_surface.values.tolist(),
                                                           x=np.array(bc_surface.columns),
                                                           y=np.array(bc_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'bc'))

            # data+bc
            data_bc_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'data_bc_surface.csv'))
            data_bc_surface = data_bc_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=data_bc_surface.values.tolist(),
                                                           x=np.array(data_bc_surface.columns),
                                                           y=np.array(data_bc_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'data+bc'))

            # bc+pinn
            bc_pinn_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'bc_pinn_surface.csv'))
            bc_pinn_surface = bc_pinn_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=bc_pinn_surface.values.tolist(),
                                                           x=np.array(bc_pinn_surface.columns),
                                                           y=np.array(bc_pinn_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'bc+pinn'))

            # data+pinn
            data_pinn_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'data_pinn_surface.csv'))
            data_pinn_surface = data_pinn_surface.set_index('Unnamed: 0')
            prediction_surface_figure.add_trace(go.Surface(z=data_pinn_surface.values.tolist(),
                                                           x=np.array(data_pinn_surface.columns),
                                                           y=np.array(data_pinn_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'data+pinn'))

            # data+bc+pinn
            data_bc_pinn_surface = pd.read_csv(os.path.join('loss_csv/dash', folder, path, 'data_bc_pinn_surface.csv'))
            data_bc_pinn_surface = data_bc_pinn_surface.set_index('Unnamed: 0')

            prediction_surface_figure.add_trace(go.Surface(z=data_bc_pinn_surface.values.tolist(),
                                                           x=np.array(data_bc_pinn_surface.columns),
                                                           y=np.array(data_bc_pinn_surface.index),
                                                           opacity=0.4, colorscale=[[0, 'red'], [1, 'red']],
                                                           showscale=False, name=folder + 'data+bc+pinn'))

            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'data'))
            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'pinn'))
            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'bc'))

            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'data+bc'))
            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'bc+pinn'))
            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'data+pinn'))

            prediction_surface_figure.update_traces(visible=False, selector=dict(name=folder + 'data+bc+pinn'))

