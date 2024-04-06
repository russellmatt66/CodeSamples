import vtk

# define source
cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(10)

# define mapper
coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

# define actor
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

# define Second Cone
# source
cone2 = vtk.vtkConeSource()
cone2.SetHeight(2.0)
cone2.SetRadius(2.0)
cone2.SetResolution(80)

# mapper 
coneMapper2 = vtk.vtkPolyDataMapper()
coneMapper2.SetInputConnection(cone2.GetOutputPort())

# actor
coneActor2 = vtk.vtkActor()
coneActor2.SetMapper(coneMapper2)

# define color
coneActor.GetProperty().SetColor(1,0,0)
coneActor2.GetProperty().SetColor(0,1,0)

# Position and orientation
cone2.SetCenter(3.5,0,0)
cone.SetDirection(0.8, 0.3, 0.5)

# define renderer
ren = vtk.vtkRenderer()
ren.AddActor(coneActor)
ren.AddActor(coneActor2)
ren.SetBackground(0.1, 0.2, 0.4)

# define rendering window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(300, 300)

# define interactor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()
