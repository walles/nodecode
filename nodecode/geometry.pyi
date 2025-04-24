# Generated from Blender 4.4.1 on 2025-04-21 16:52:34
from typing import Any, Tuple

class AccumulateField:
    """Add the values of an evaluated field together and output the running total for each element"""
    def __init__(
        self, data_type: Any, domain: Any, Value: float = ..., Group_ID: int = ...
    ) -> None: ...
    def Leading(self) -> float:
        """Leading"""
    def Trailing(self) -> float:
        """Trailing"""
    def Total(self) -> float:
        """Total"""

class AttributeDomainSize:
    """Retrieve the number of elements in a geometry for each attribute domain"""
    def __init__(self, component: Any, Geometry: Any = ...) -> None: ...
    def Point_Count(self) -> int:
        """Point Count"""
    def Edge_Count(self) -> int:
        """Edge Count"""
    def Face_Count(self) -> int:
        """Face Count"""
    def Face_Corner_Count(self) -> int:
        """Face Corner Count"""
    def Spline_Count(self) -> int:
        """Spline Count"""
    def Instance_Count(self) -> int:
        """Instance Count"""
    def Layer_Count(self) -> int:
        """Layer Count"""

class AttributeStatistic:
    """Calculate statistics about a data set from a field evaluated on a geometry"""
    def __init__(
        self,
        data_type: Any,
        domain: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Attribute: float = ...,
    ) -> None: ...
    def Mean(self) -> float:
        """Mean"""
    def Median(self) -> float:
        """Median"""
    def Sum(self) -> float:
        """Sum"""
    def Min(self) -> float:
        """Min"""
    def Max(self) -> float:
        """Max"""
    def Range(self) -> float:
        """Range"""
    def Standard_Deviation(self) -> float:
        """Standard Deviation"""
    def Variance(self) -> float:
        """Variance"""

class Bake:
    """Cache the incoming data so that it can be used without recomputation"""
    def __init__(
        self, active_index: int, active_item: Any, Geometry: Any = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class BlurAttribute:
    """Mix attribute values of neighboring elements"""
    def __init__(
        self,
        data_type: Any,
        Value: float = ...,
        Iterations: int = ...,
        Weight: float = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""

class BoundBox:
    """Calculate the limits of a geometry's positions and generate a box mesh with those dimensions"""
    def __init__(self, Geometry: Any = ...) -> None: ...
    def Bounding_Box(self) -> Any:
        """Bounding Box"""
    def Min(self) -> Tuple[float, float, float]:
        """Min"""
    def Max(self) -> Tuple[float, float, float]:
        """Max"""

class CaptureAttribute:
    """Store the result of a field on a geometry and output the data as a node socket. Allows remembering or interpolating data as the geometry changes, such as positions before deformation"""
    def __init__(
        self, active_index: int, active_item: Any, domain: Any, Geometry: Any = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class CollectionInfo:
    """Retrieve geometry instances from a collection"""
    def __init__(
        self,
        transform_space: Any,
        Collection: Any = ...,
        Separate_Children: bool = ...,
        Reset_Children: bool = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class ConvexHull:
    """Create a mesh that encloses all points in the input geometry with the smallest number of points"""
    def __init__(self, Geometry: Any = ...) -> None: ...
    def Convex_Hull(self) -> Any:
        """Convex Hull"""

class CornersOfEdge:
    """Retrieve face corners connected to edges"""
    def __init__(
        self, Edge_Index: int = ..., Weights: float = ..., Sort_Index: int = ...
    ) -> None: ...
    def Corner_Index(self) -> int:
        """Corner Index"""
    def Total(self) -> int:
        """Total"""

class CornersOfFace:
    """Retrieve corners that make up a face"""
    def __init__(
        self, Face_Index: int = ..., Weights: float = ..., Sort_Index: int = ...
    ) -> None: ...
    def Corner_Index(self) -> int:
        """Corner Index"""
    def Total(self) -> int:
        """Total"""

class CornersOfVertex:
    """Retrieve face corners connected to vertices"""
    def __init__(
        self, Vertex_Index: int = ..., Weights: float = ..., Sort_Index: int = ...
    ) -> None: ...
    def Corner_Index(self) -> int:
        """Corner Index"""
    def Total(self) -> int:
        """Total"""

class CurveArc:
    """Generate a poly spline arc"""
    def __init__(
        self,
        mode: Any,
        Resolution: int = ...,
        Start: Tuple[float, float, float] = ...,
        Middle: Tuple[float, float, float] = ...,
        End: Tuple[float, float, float] = ...,
        Radius: float = ...,
        Start_Angle: float = ...,
        Sweep_Angle: float = ...,
        Offset_Angle: float = ...,
        Connect_Center: bool = ...,
        Invert_Arc: bool = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""
    def Center(self) -> Tuple[float, float, float]:
        """Center"""
    def Normal(self) -> Tuple[float, float, float]:
        """Normal"""
    def Radius(self) -> float:
        """Radius"""

class CurveEndpointSelection:
    """Provide a selection for an arbitrary number of endpoints in each spline"""
    def __init__(self, Start_Size: int = ..., End_Size: int = ...) -> None: ...
    def Selection(self) -> bool:
        """Selection"""

class CurveHandleTypeSelection:
    """Provide a selection based on the handle types of Bézier control points"""
    def __init__(self, handle_type: Any, mode: Any) -> None: ...
    def Selection(self) -> bool:
        """Selection"""

class CurveLength:
    """Retrieve the length of all splines added together"""
    def __init__(self, Curve: Any = ...) -> None: ...
    def Length(self) -> float:
        """Length"""

class CurveOfPoint:
    """Retrieve the curve a control point is part of"""
    def __init__(self, Point_Index: int = ...) -> None: ...
    def Curve_Index(self) -> int:
        """Curve Index"""
    def Index_in_Curve(self) -> int:
        """Index in Curve"""

class CurvePrimitiveBezierSegment:
    """Generate a 2D Bézier spline from the given control points and handles"""
    def __init__(
        self,
        mode: Any,
        Resolution: int = ...,
        Start: Tuple[float, float, float] = ...,
        Start_Handle: Tuple[float, float, float] = ...,
        End_Handle: Tuple[float, float, float] = ...,
        End: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurvePrimitiveCircle:
    """Generate a poly spline circle"""
    def __init__(
        self,
        mode: Any,
        Resolution: int = ...,
        Point_1: Tuple[float, float, float] = ...,
        Point_2: Tuple[float, float, float] = ...,
        Point_3: Tuple[float, float, float] = ...,
        Radius: float = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""
    def Center(self) -> Tuple[float, float, float]:
        """Center"""

class CurvePrimitiveLine:
    """Generate a poly spline line with two points"""
    def __init__(
        self,
        mode: Any,
        Start: Tuple[float, float, float] = ...,
        End: Tuple[float, float, float] = ...,
        Direction: Tuple[float, float, float] = ...,
        Length: float = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurvePrimitiveQuadrilateral:
    """Generate a polygon with four points"""
    def __init__(
        self,
        mode: Any,
        Width: float = ...,
        Height: float = ...,
        Bottom_Width: float = ...,
        Top_Width: float = ...,
        Offset: float = ...,
        Bottom_Height: float = ...,
        Top_Height: float = ...,
        Point_1: Tuple[float, float, float] = ...,
        Point_2: Tuple[float, float, float] = ...,
        Point_3: Tuple[float, float, float] = ...,
        Point_4: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurveQuadraticBezier:
    """Generate a poly spline in a parabola shape with control points positions"""
    def __init__(
        self,
        Resolution: int = ...,
        Start: Tuple[float, float, float] = ...,
        Middle: Tuple[float, float, float] = ...,
        End: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurveSetHandles:
    """Set the handle type for the control points of a Bézier curve"""
    def __init__(
        self, handle_type: Any, mode: Any, Curve: Any = ..., Selection: bool = ...
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurveSpiral:
    """Generate a poly spline in a spiral shape"""
    def __init__(
        self,
        Resolution: int = ...,
        Rotations: float = ...,
        Start_Radius: float = ...,
        End_Radius: float = ...,
        Height: float = ...,
        Reverse: bool = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurveSplineType:
    """Change the type of curves"""
    def __init__(
        self, spline_type: Any, Curve: Any = ..., Selection: bool = ...
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class CurveStar:
    """Generate a poly spline in a star pattern by connecting alternating points of two circles"""
    def __init__(
        self,
        Points: int = ...,
        Inner_Radius: float = ...,
        Outer_Radius: float = ...,
        Twist: float = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""
    def Outer_Points(self) -> bool:
        """Outer Points"""

class CurveToMesh:
    """Convert curves into a mesh, optionally with a custom profile shape defined by curves"""
    def __init__(
        self, Curve: Any = ..., Profile_Curve: Any = ..., Fill_Caps: bool = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class CurveToPoints:
    """Generate a point cloud by sampling positions along curves"""
    def __init__(
        self, mode: Any, Curve: Any = ..., Count: int = ..., Length: float = ...
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""
    def Tangent(self) -> Tuple[float, float, float]:
        """Tangent"""
    def Normal(self) -> Tuple[float, float, float]:
        """Normal"""
    def Rotation(self) -> Any:
        """Rotation"""

class CurvesToGreasePencil:
    """Convert the curves in each top-level instance into Grease Pencil layer"""
    def __init__(
        self, Curves: Any = ..., Selection: bool = ..., Instances_as_Layers: bool = ...
    ) -> None: ...
    def Grease_Pencil(self) -> Any:
        """Grease Pencil"""

class DeformCurvesOnSurface:
    """Translate and rotate curves based on changes between the object's original and evaluated surface mesh"""
    def __init__(self, Curves: Any = ...) -> None: ...
    def Curves(self) -> Any:
        """Curves"""

class DeleteGeometry:
    """Remove selected elements of a geometry"""
    def __init__(
        self, mode: Any, domain: Any, Geometry: Any = ..., Selection: bool = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class DistributePointsInGrid:
    """Generate points inside a volume grid"""
    def __init__(
        self,
        mode: Any,
        Grid: float = ...,
        Density: float = ...,
        Seed: int = ...,
        Spacing: Tuple[float, float, float] = ...,
        Threshold: float = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class DistributePointsInVolume:
    """Generate points inside a volume"""
    def __init__(
        self,
        mode: Any,
        Volume: Any = ...,
        Density: float = ...,
        Seed: int = ...,
        Spacing: Tuple[float, float, float] = ...,
        Threshold: float = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class DistributePointsOnFaces:
    """Generate points spread out on the surface of a mesh"""
    def __init__(
        self,
        distribute_method: Any,
        use_legacy_normal: bool,
        Mesh: Any = ...,
        Selection: bool = ...,
        Distance_Min: float = ...,
        Density_Max: float = ...,
        Density: float = ...,
        Density_Factor: float = ...,
        Seed: int = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""
    def Normal(self) -> Tuple[float, float, float]:
        """Normal"""
    def Rotation(self) -> Any:
        """Rotation"""

class DualMesh:
    """Convert Faces into vertices and vertices into faces"""
    def __init__(self, Mesh: Any = ..., Keep_Boundaries: bool = ...) -> None: ...
    def Dual_Mesh(self) -> Any:
        """Dual Mesh"""

class DuplicateElements:
    """Generate an arbitrary number copies of each selected input element"""
    def __init__(
        self, domain: Any, Geometry: Any = ..., Selection: bool = ..., Amount: int = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""
    def Duplicate_Index(self) -> int:
        """Duplicate Index"""

class EdgePathsToCurves:
    """Output curves following paths across mesh edges"""
    def __init__(
        self, Mesh: Any = ..., Start_Vertices: bool = ..., Next_Vertex_Index: int = ...
    ) -> None: ...
    def Curves(self) -> Any:
        """Curves"""

class EdgePathsToSelection:
    """Output a selection of edges by following paths across mesh edges"""
    def __init__(
        self, Start_Vertices: bool = ..., Next_Vertex_Index: int = ...
    ) -> None: ...
    def Selection(self) -> bool:
        """Selection"""

class EdgesOfCorner:
    """Retrieve the edges on both sides of a face corner"""
    def __init__(self, Corner_Index: int = ...) -> None: ...
    def Next_Edge_Index(self) -> int:
        """Next Edge Index"""
    def Previous_Edge_Index(self) -> int:
        """Previous Edge Index"""

class EdgesOfVertex:
    """Retrieve the edges connected to each vertex"""
    def __init__(
        self, Vertex_Index: int = ..., Weights: float = ..., Sort_Index: int = ...
    ) -> None: ...
    def Edge_Index(self) -> int:
        """Edge Index"""
    def Total(self) -> int:
        """Total"""

class EdgesToFaceGroups:
    """Group faces into regions surrounded by the selected boundary edges"""
    def __init__(self, Boundary_Edges: bool = ...) -> None: ...
    def Face_Group_ID(self) -> int:
        """Face Group ID"""

class ExtrudeMesh:
    """Generate new vertices, edges, or faces from selected elements and move them based on an offset while keeping them connected by their boundary"""
    def __init__(
        self,
        mode: Any,
        Mesh: Any = ...,
        Selection: bool = ...,
        Offset: Tuple[float, float, float] = ...,
        Offset_Scale: float = ...,
        Individual: bool = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def Top(self) -> bool:
        """Top"""
    def Side(self) -> bool:
        """Side"""

class FaceOfCorner:
    """Retrieve the face each face corner is part of"""
    def __init__(self, Corner_Index: int = ...) -> None: ...
    def Face_Index(self) -> int:
        """Face Index"""
    def Index_in_Face(self) -> int:
        """Index in Face"""

class FieldAtIndex:
    """Retrieve data of other elements in the context's geometry"""
    def __init__(
        self, domain: Any, data_type: Any, Index: int = ..., Value: float = ...
    ) -> None: ...
    def Value(self) -> float:
        """Value"""

class FieldOnDomain:
    """Retrieve values from a field on a different domain besides the domain from the context"""
    def __init__(self, domain: Any, data_type: Any, Value: float = ...) -> None: ...
    def Value(self) -> float:
        """Value"""

class FillCurve:
    """Generate a mesh on the XY plane with faces on the inside of input curves"""
    def __init__(self, mode: Any, Curve: Any = ..., Group_ID: int = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class FilletCurve:
    """Round corners by generating circular arcs on each control point"""
    def __init__(
        self,
        mode: Any,
        Curve: Any = ...,
        Count: int = ...,
        Radius: float = ...,
        Limit_Radius: bool = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class FlipFaces:
    """Reverse the order of the vertices and edges of selected faces, flipping their normal direction"""
    def __init__(self, Mesh: Any = ..., Selection: bool = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class ForeachGeometryElementInput:
    """For Each Geometry Element Input"""
    def __init__(self, Geometry: Any = ..., Selection: bool = ...) -> None: ...
    def Index(self) -> int:
        """Index"""
    def Element(self) -> Any:
        """Element"""

class ForeachGeometryElementOutput:
    """For Each Geometry Element Output"""
    def __init__(
        self,
        active_input_index: int,
        active_generation_index: int,
        active_main_index: int,
        domain: Any,
        inspection_index: int,
        Geometry: Any = ...,
    ) -> None: ...
    def Geometry1(self) -> Any:
        """Geometry"""
    def Geometry2(self) -> Any:
        """Geometry"""

class GeometryToInstance:
    """Convert each input geometry into an instance, which can be much faster than the Join Geometry node when the inputs are large"""
    def __init__(self, Geometry: Any = ...) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class GetNamedGrid:
    """Get volume grid from a volume geometry with the specified name"""
    def __init__(
        self, data_type: Any, Volume: Any = ..., Name: str = ..., Remove: bool = ...
    ) -> None: ...
    def Volume(self) -> Any:
        """Volume"""
    def Grid(self) -> float:
        """Grid"""

class GizmoDial:
    """Show a dial gizmo in the viewport for a value"""
    def __init__(
        self,
        color_id: Any,
        Value: float = ...,
        Position: Tuple[float, float, float] = ...,
        Up: Tuple[float, float, float] = ...,
        Screen_Space: bool = ...,
        Radius: float = ...,
    ) -> None: ...
    def Transform(self) -> Any:
        """Transform"""

class GizmoLinear:
    """Show a linear gizmo in the viewport for a value"""
    def __init__(
        self,
        color_id: Any,
        draw_style: Any,
        Value: float = ...,
        Position: Tuple[float, float, float] = ...,
        Direction: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Transform(self) -> Any:
        """Transform"""

class GizmoTransform:
    """Show a transform gizmo in the viewport"""
    def __init__(
        self,
        use_translation_x: bool,
        use_translation_y: bool,
        use_translation_z: bool,
        use_rotation_x: bool,
        use_rotation_y: bool,
        use_rotation_z: bool,
        use_scale_x: bool,
        use_scale_y: bool,
        use_scale_z: bool,
        Value: Any = ...,
        Position: Tuple[float, float, float] = ...,
        Rotation: Any = ...,
    ) -> None: ...
    def Transform(self) -> Any:
        """Transform"""

class GreasePencilToCurves:
    """Convert Grease Pencil layers into curve instances"""
    def __init__(
        self,
        Grease_Pencil: Any = ...,
        Selection: bool = ...,
        Layers_as_Instances: bool = ...,
    ) -> None: ...
    def Curves(self) -> Any:
        """Curves"""

class GridToMesh:
    """Generate a mesh on the "surface" of a volume grid"""
    def __init__(
        self, Grid: float = ..., Threshold: float = ..., Adaptivity: float = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class Group:
    """Group"""
    def __init__(self, node_tree: Any) -> None: ...

class ImageInfo:
    """Retrieve information about an image"""
    def __init__(self, Image: Any = ..., Frame: int = ...) -> None: ...
    def Width(self) -> int:
        """Width"""
    def Height(self) -> int:
        """Height"""
    def Has_Alpha(self) -> bool:
        """Has Alpha"""
    def Frame_Count(self) -> int:
        """Frame Count"""
    def FPS(self) -> float:
        """FPS"""

class ImageTexture:
    """Sample values from an image texture"""
    def __init__(
        self,
        interpolation: Any,
        extension: Any,
        Image: Any = ...,
        Vector: Tuple[float, float, float] = ...,
        Frame: int = ...,
    ) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]:
        """Color"""
    def Alpha(self) -> float:
        """Alpha"""

class ImportOBJ:
    """Import geometry from an OBJ file"""
    def __init__(self, Path: str = ...) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class ImportPLY:
    """Import a point cloud from a PLY file"""
    def __init__(self, Path: str = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class ImportSTL:
    """Import a mesh from an STL file"""
    def __init__(self, Path: str = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class IndexOfNearest:
    """Find the nearest element in a group. Similar to the "Sample Nearest" node"""
    def __init__(
        self, Position: Tuple[float, float, float] = ..., Group_ID: int = ...
    ) -> None: ...
    def Index(self) -> int:
        """Index"""
    def Has_Neighbor(self) -> bool:
        """Has Neighbor"""

class IndexSwitch:
    """Choose between an arbitrary number of values with an index"""
    def __init__(
        self, data_type: Any, Index: int = ..., _0: Any = ..., _1: Any = ...
    ) -> None: ...
    def Output(self) -> Any:
        """Output"""

class InputActiveCamera:
    """Retrieve the scene's active camera"""
    def __init__(
        self,
    ) -> None: ...
    def Active_Camera(self) -> Any:
        """Active Camera"""

class InputCollection:
    """Output a single collection"""
    def __init__(self, collection: Any) -> None: ...
    def Collection(self) -> Any:
        """Collection"""

class InputCurveHandlePositions:
    """Retrieve the position of each Bézier control point's handles"""
    def __init__(self, Relative: bool = ...) -> None: ...
    def Left(self) -> Tuple[float, float, float]:
        """Left"""
    def Right(self) -> Tuple[float, float, float]:
        """Right"""

class InputCurveTilt:
    """Retrieve the angle at each control point used to twist the curve's normal around its tangent"""
    def __init__(
        self,
    ) -> None: ...
    def Tilt(self) -> float:
        """Tilt"""

class InputEdgeSmooth:
    """Retrieve whether each edge is marked for smooth or split normals"""
    def __init__(
        self,
    ) -> None: ...
    def Smooth(self) -> bool:
        """Smooth"""

class InputID:
    """Retrieve a stable random identifier value from the "id" attribute on the point domain, or the index if the attribute does not exist"""
    def __init__(
        self,
    ) -> None: ...
    def ID(self) -> int:
        """ID"""

class InputImage:
    """Input an image data-block"""
    def __init__(self, image: Any) -> None: ...
    def Image(self) -> Any:
        """Image"""

class InputIndex:
    """Retrieve an integer value indicating the position of each element in the list, starting at zero"""
    def __init__(
        self,
    ) -> None: ...
    def Index(self) -> int:
        """Index"""

class InputInstanceRotation:
    """Retrieve the rotation of each instance in the geometry"""
    def __init__(
        self,
    ) -> None: ...
    def Rotation(self) -> Any:
        """Rotation"""

class InputInstanceScale:
    """Retrieve the scale of each instance in the geometry"""
    def __init__(
        self,
    ) -> None: ...
    def Scale(self) -> Tuple[float, float, float]:
        """Scale"""

class InputMaterial:
    """Output a single material"""
    def __init__(self, material: Any) -> None: ...
    def Material(self) -> Any:
        """Material"""

class InputMaterialIndex:
    """Retrieve the index of the material used for each element in the geometry's list of materials"""
    def __init__(
        self,
    ) -> None: ...
    def Material_Index(self) -> int:
        """Material Index"""

class InputMeshEdgeAngle:
    """The angle between the normals of connected manifold faces"""
    def __init__(
        self,
    ) -> None: ...
    def Unsigned_Angle(self) -> float:
        """Unsigned Angle"""
    def Signed_Angle(self) -> float:
        """Signed Angle"""

class InputMeshEdgeNeighbors:
    """Retrieve the number of faces that use each edge as one of their sides"""
    def __init__(
        self,
    ) -> None: ...
    def Face_Count(self) -> int:
        """Face Count"""

class InputMeshEdgeVertices:
    """Retrieve topology information relating to each edge of a mesh"""
    def __init__(
        self,
    ) -> None: ...
    def Vertex_Index_1(self) -> int:
        """Vertex Index 1"""
    def Vertex_Index_2(self) -> int:
        """Vertex Index 2"""
    def Position_1(self) -> Tuple[float, float, float]:
        """Position 1"""
    def Position_2(self) -> Tuple[float, float, float]:
        """Position 2"""

class InputMeshFaceArea:
    """Calculate the surface area of a mesh's faces"""
    def __init__(
        self,
    ) -> None: ...
    def Area(self) -> float:
        """Area"""

class InputMeshFaceIsPlanar:
    """Retrieve whether all triangles in a face are on the same plane, i.e. whether they have the same normal"""
    def __init__(self, Threshold: float = ...) -> None: ...
    def Planar(self) -> bool:
        """Planar"""

class InputMeshFaceNeighbors:
    """Retrieve topology information relating to each face of a mesh"""
    def __init__(
        self,
    ) -> None: ...
    def Vertex_Count(self) -> int:
        """Vertex Count"""
    def Face_Count(self) -> int:
        """Face Count"""

class InputMeshIsland:
    """Retrieve information about separate connected regions in a mesh"""
    def __init__(
        self,
    ) -> None: ...
    def Island_Index(self) -> int:
        """Island Index"""
    def Island_Count(self) -> int:
        """Island Count"""

class InputMeshVertexNeighbors:
    """Retrieve topology information relating to each vertex of a mesh"""
    def __init__(
        self,
    ) -> None: ...
    def Vertex_Count(self) -> int:
        """Vertex Count"""
    def Face_Count(self) -> int:
        """Face Count"""

class InputNamedAttribute:
    """Retrieve the data of a specified attribute"""
    def __init__(self, data_type: Any, Name: str = ...) -> None: ...
    def Attribute(self) -> float:
        """Attribute"""
    def Exists(self) -> bool:
        """Exists"""

class InputNamedLayerSelection:
    """Output a selection of a Grease Pencil layer"""
    def __init__(self, Name: str = ...) -> None: ...
    def Selection(self) -> bool:
        """Selection"""

class InputNormal:
    """Retrieve a unit length vector indicating the direction pointing away from the geometry at each element"""
    def __init__(self, legacy_corner_normals: bool) -> None: ...
    def Normal(self) -> Tuple[float, float, float]:
        """Normal"""

class InputObject:
    """Output a single object"""
    def __init__(self, object: Any) -> None: ...
    def Object(self) -> Any:
        """Object"""

class InputPosition:
    """Retrieve a vector indicating the location of each element"""
    def __init__(
        self,
    ) -> None: ...
    def Position(self) -> Tuple[float, float, float]:
        """Position"""

class InputRadius:
    """Retrieve the radius at each point on curve or point cloud geometry"""
    def __init__(
        self,
    ) -> None: ...
    def Radius(self) -> float:
        """Radius"""

class InputSceneTime:
    """Retrieve the current time in the scene's animation in units of seconds or frames"""
    def __init__(
        self,
    ) -> None: ...
    def Seconds(self) -> float:
        """Seconds"""
    def Frame(self) -> float:
        """Frame"""

class InputShadeSmooth:
    """Retrieve whether each face is marked for smooth or sharp normals"""
    def __init__(
        self,
    ) -> None: ...
    def Smooth(self) -> bool:
        """Smooth"""

class InputShortestEdgePaths:
    """Find the shortest paths along mesh edges to selected end vertices, with customizable cost per edge"""
    def __init__(self, End_Vertex: bool = ..., Edge_Cost: float = ...) -> None: ...
    def Next_Vertex_Index(self) -> int:
        """Next Vertex Index"""
    def Total_Cost(self) -> float:
        """Total Cost"""

class InputSplineCyclic:
    """Retrieve whether each spline endpoint connects to the beginning"""
    def __init__(
        self,
    ) -> None: ...
    def Cyclic(self) -> bool:
        """Cyclic"""

class InputSplineResolution:
    """Retrieve the number of evaluated points that will be generated for every control point on curves"""
    def __init__(
        self,
    ) -> None: ...
    def Resolution(self) -> int:
        """Resolution"""

class InputTangent:
    """Retrieve the direction of curves at each control point"""
    def __init__(
        self,
    ) -> None: ...
    def Tangent(self) -> Tuple[float, float, float]:
        """Tangent"""

class InstanceOnPoints:
    """Generate a reference to geometry at each of the input points, without duplicating its underlying data"""
    def __init__(
        self,
        Points: Any = ...,
        Selection: bool = ...,
        Instance: Any = ...,
        Pick_Instance: bool = ...,
        Instance_Index: int = ...,
        Rotation: Any = ...,
        Scale: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class InstanceTransform:
    """Retrieve the full transformation of each instance in the geometry"""
    def __init__(
        self,
    ) -> None: ...
    def Transform(self) -> Any:
        """Transform"""

class InstancesToPoints:
    """Generate points at the origins of instances.

    Note: Nested instances are not affected by this node"""
    def __init__(
        self,
        Instances: Any = ...,
        Selection: bool = ...,
        Position: Tuple[float, float, float] = ...,
        Radius: float = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class InterpolateCurves:
    """Generate new curves on points by interpolating between existing curves"""
    def __init__(
        self,
        Guide_Curves: Any = ...,
        Guide_Up: Tuple[float, float, float] = ...,
        Guide_Group_ID: int = ...,
        Points: Any = ...,
        Point_Up: Tuple[float, float, float] = ...,
        Point_Group_ID: int = ...,
        Max_Neighbors: int = ...,
    ) -> None: ...
    def Curves(self) -> Any:
        """Curves"""
    def Closest_Index(self) -> int:
        """Closest Index"""
    def Closest_Weight(self) -> float:
        """Closest Weight"""

class IsViewport:
    """Retrieve whether the nodes are being evaluated for the viewport rather than the final render"""
    def __init__(
        self,
    ) -> None: ...
    def Is_Viewport(self) -> bool:
        """Is Viewport"""

class JoinGeometry:
    """Merge separately generated geometries into a single one"""
    def __init__(self, Geometry: Any = ...) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class MaterialSelection:
    """Provide a selection of faces that use the specified material"""
    def __init__(self, Material: Any = ...) -> None: ...
    def Selection(self) -> bool:
        """Selection"""

class MenuSwitch:
    """Select from multiple inputs by name"""
    def __init__(
        self,
        active_index: int,
        active_item: Any,
        data_type: Any,
        Menu: Any = ...,
        A: Any = ...,
        B: Any = ...,
    ) -> None: ...
    def Output(self) -> Any:
        """Output"""

class MergeByDistance:
    """Merge vertices or points within a given distance"""
    def __init__(
        self,
        mode: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Distance: float = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class MergeLayers:
    """Join groups of Grease Pencil layers into one"""
    def __init__(
        self,
        mode: Any,
        Grease_Pencil: Any = ...,
        Selection: bool = ...,
        Group_ID: int = ...,
    ) -> None: ...
    def Grease_Pencil(self) -> Any:
        """Grease Pencil"""

class MeshBoolean:
    """Cut, subtract, or join multiple mesh inputs"""
    def __init__(
        self,
        operation: Any,
        solver: Any,
        Mesh_1: Any = ...,
        Mesh_2: Any = ...,
        Self_Intersection: bool = ...,
        Hole_Tolerant: bool = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def Intersecting_Edges(self) -> bool:
        """Intersecting Edges"""

class MeshCircle:
    """Generate a circular ring of edges"""
    def __init__(
        self, fill_type: Any, Vertices: int = ..., Radius: float = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class MeshCone:
    """Generate a cone mesh"""
    def __init__(
        self,
        fill_type: Any,
        Vertices: int = ...,
        Side_Segments: int = ...,
        Fill_Segments: int = ...,
        Radius_Top: float = ...,
        Radius_Bottom: float = ...,
        Depth: float = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def Top(self) -> bool:
        """Top"""
    def Bottom(self) -> bool:
        """Bottom"""
    def Side(self) -> bool:
        """Side"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class MeshCube:
    """Generate a cuboid mesh with variable side lengths and subdivisions"""
    def __init__(
        self,
        Size: Tuple[float, float, float] = ...,
        Vertices_X: int = ...,
        Vertices_Y: int = ...,
        Vertices_Z: int = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class MeshCylinder:
    """Generate a cylinder mesh"""
    def __init__(
        self,
        fill_type: Any,
        Vertices: int = ...,
        Side_Segments: int = ...,
        Fill_Segments: int = ...,
        Radius: float = ...,
        Depth: float = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def Top(self) -> bool:
        """Top"""
    def Side(self) -> bool:
        """Side"""
    def Bottom(self) -> bool:
        """Bottom"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class MeshFaceSetBoundaries:
    """Find edges on the boundaries between groups of faces with the same ID value"""
    def __init__(self, Face_Group_ID: int = ...) -> None: ...
    def Boundary_Edges(self) -> bool:
        """Boundary Edges"""

class MeshGrid:
    """Generate a planar mesh on the XY plane"""
    def __init__(
        self,
        Size_X: float = ...,
        Size_Y: float = ...,
        Vertices_X: int = ...,
        Vertices_Y: int = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class MeshIcoSphere:
    """Generate a spherical mesh that consists of equally sized triangles"""
    def __init__(self, Radius: float = ..., Subdivisions: int = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class MeshLine:
    """Generate vertices in a line and connect them with edges"""
    def __init__(
        self,
        mode: Any,
        count_mode: Any,
        Count: int = ...,
        Resolution: float = ...,
        Start_Location: Tuple[float, float, float] = ...,
        Offset: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class MeshToCurve:
    """Generate a curve from a mesh"""
    def __init__(self, Mesh: Any = ..., Selection: bool = ...) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class MeshToDensityGrid:
    """Create a filled volume grid from a mesh"""
    def __init__(
        self,
        Mesh: Any = ...,
        Density: float = ...,
        Voxel_Size: float = ...,
        Gradient_Width: float = ...,
    ) -> None: ...
    def Density_Grid(self) -> float:
        """Density Grid"""

class MeshToPoints:
    """Generate a point cloud from a mesh's vertices"""
    def __init__(
        self,
        mode: Any,
        Mesh: Any = ...,
        Selection: bool = ...,
        Position: Tuple[float, float, float] = ...,
        Radius: float = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class MeshToSDFGrid:
    """Create a signed distance volume grid from a mesh"""
    def __init__(
        self, Mesh: Any = ..., Voxel_Size: float = ..., Band_Width: int = ...
    ) -> None: ...
    def SDF_Grid(self) -> float:
        """SDF Grid"""

class MeshToVolume:
    """Create a fog volume with the shape of the input mesh's surface"""
    def __init__(
        self,
        resolution_mode: Any,
        Mesh: Any = ...,
        Density: float = ...,
        Voxel_Size: float = ...,
        Voxel_Amount: float = ...,
        Interior_Band_Width: float = ...,
    ) -> None: ...
    def Volume(self) -> Any:
        """Volume"""

class MeshUVSphere:
    """Generate a spherical mesh with quads, except for triangles at the top and bottom"""
    def __init__(
        self, Segments: int = ..., Rings: int = ..., Radius: float = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def UV_Map(self) -> Tuple[float, float, float]:
        """UV Map"""

class ObjectInfo:
    """Retrieve information from an object"""
    def __init__(
        self, transform_space: Any, Object: Any = ..., As_Instance: bool = ...
    ) -> None: ...
    def Transform(self) -> Any:
        """Transform"""
    def Location(self) -> Tuple[float, float, float]:
        """Location"""
    def Rotation(self) -> Any:
        """Rotation"""
    def Scale(self) -> Tuple[float, float, float]:
        """Scale"""
    def Geometry(self) -> Any:
        """Geometry"""

class OffsetCornerInFace:
    """Retrieve corners in the same face as another"""
    def __init__(self, Corner_Index: int = ..., Offset: int = ...) -> None: ...
    def Corner_Index(self) -> int:
        """Corner Index"""

class OffsetPointInCurve:
    """Offset a control point index within its curve"""
    def __init__(self, Point_Index: int = ..., Offset: int = ...) -> None: ...
    def Is_Valid_Offset(self) -> bool:
        """Is Valid Offset"""
    def Point_Index(self) -> int:
        """Point Index"""

class Points:
    """Generate a point cloud with positions and radii defined by fields"""
    def __init__(
        self,
        Count: int = ...,
        Position: Tuple[float, float, float] = ...,
        Radius: float = ...,
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class PointsOfCurve:
    """Retrieve a point index within a curve"""
    def __init__(
        self, Curve_Index: int = ..., Weights: float = ..., Sort_Index: int = ...
    ) -> None: ...
    def Point_Index(self) -> int:
        """Point Index"""
    def Total(self) -> int:
        """Total"""

class PointsToCurves:
    """Split all points to curve by its group ID and reorder by weight"""
    def __init__(
        self, Points: Any = ..., Curve_Group_ID: int = ..., Weight: float = ...
    ) -> None: ...
    def Curves(self) -> Any:
        """Curves"""

class PointsToSDFGrid:
    """Create a signed distance volume grid from points"""
    def __init__(
        self, Points: Any = ..., Radius: float = ..., Voxel_Size: float = ...
    ) -> None: ...
    def SDF_Grid(self) -> float:
        """SDF Grid"""

class PointsToVertices:
    """Generate a mesh vertex for each point cloud point"""
    def __init__(self, Points: Any = ..., Selection: bool = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class PointsToVolume:
    """Generate a fog volume sphere around every point"""
    def __init__(
        self,
        resolution_mode: Any,
        Points: Any = ...,
        Density: float = ...,
        Voxel_Size: float = ...,
        Voxel_Amount: float = ...,
        Radius: float = ...,
    ) -> None: ...
    def Volume(self) -> Any:
        """Volume"""

class Proximity:
    """Compute the closest location on the target geometry"""
    def __init__(
        self,
        target_element: Any,
        Geometry: Any = ...,
        Group_ID: int = ...,
        Sample_Position: Tuple[float, float, float] = ...,
        Sample_Group_ID: int = ...,
    ) -> None: ...
    def Position(self) -> Tuple[float, float, float]:
        """Position"""
    def Distance(self) -> float:
        """Distance"""
    def Is_Valid(self) -> bool:
        """Is Valid"""

class Raycast:
    """Cast rays from the context geometry onto a target geometry, and retrieve information from each hit point"""
    def __init__(
        self,
        mapping: Any,
        data_type: Any,
        Target_Geometry: Any = ...,
        Attribute: float = ...,
        Source_Position: Tuple[float, float, float] = ...,
        Ray_Direction: Tuple[float, float, float] = ...,
        Ray_Length: float = ...,
    ) -> None: ...
    def Is_Hit(self) -> bool:
        """Is Hit"""
    def Hit_Position(self) -> Tuple[float, float, float]:
        """Hit Position"""
    def Hit_Normal(self) -> Tuple[float, float, float]:
        """Hit Normal"""
    def Hit_Distance(self) -> float:
        """Hit Distance"""
    def Attribute(self) -> float:
        """Attribute"""

class RealizeInstances:
    """Convert instances into real geometry data"""
    def __init__(
        self,
        Geometry: Any = ...,
        Selection: bool = ...,
        Realize_All: bool = ...,
        Depth: int = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class RemoveAttribute:
    """Delete an attribute with a specified name from a geometry. Typically used to optimize performance"""
    def __init__(
        self, pattern_mode: Any, Geometry: Any = ..., Name: str = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class RepeatInput:
    """Repeat Input"""
    def __init__(self, Iterations: int = ...) -> None: ...
    def Iteration(self) -> int:
        """Iteration"""

class RepeatOutput:
    """Repeat Output"""
    def __init__(
        self,
        active_index: int,
        active_item: Any,
        inspection_index: int,
        Geometry: Any = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class ReplaceMaterial:
    """Swap one material with another"""
    def __init__(self, Geometry: Any = ..., Old: Any = ..., New: Any = ...) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class ResampleCurve:
    """Generate a poly spline for each input spline"""
    def __init__(
        self,
        mode: Any,
        keep_last_segment: bool,
        Curve: Any = ...,
        Selection: bool = ...,
        Count: int = ...,
        Length: float = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class ReverseCurve:
    """Change the direction of curves by swapping their start and end data"""
    def __init__(self, Curve: Any = ..., Selection: bool = ...) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class RotateInstances:
    """Rotate geometry instances in local or global space"""
    def __init__(
        self,
        Instances: Any = ...,
        Selection: bool = ...,
        Rotation: Any = ...,
        Pivot_Point: Tuple[float, float, float] = ...,
        Local_Space: bool = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class SDFGridBoolean:
    """Cut, subtract, or join multiple SDF volume grid inputs"""
    def __init__(
        self, operation: Any, Grid_1: float = ..., Grid_2: float = ...
    ) -> None: ...
    def Grid(self) -> float:
        """Grid"""

class SampleCurve:
    """Retrieve data from a point on a curve at a certain distance from its start"""
    def __init__(
        self,
        mode: Any,
        use_all_curves: bool,
        data_type: Any,
        Curves: Any = ...,
        Value: float = ...,
        Factor: float = ...,
        Length: float = ...,
        Curve_Index: int = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""
    def Position(self) -> Tuple[float, float, float]:
        """Position"""
    def Tangent(self) -> Tuple[float, float, float]:
        """Tangent"""
    def Normal(self) -> Tuple[float, float, float]:
        """Normal"""

class SampleGrid:
    """Sample Grid"""
    def __init__(
        self,
        data_type: Any,
        interpolation_mode: Any,
        Grid: float = ...,
        Position: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""

class SampleGridIndex:
    """Retrieve volume grid values at specific voxels"""
    def __init__(
        self,
        data_type: Any,
        Grid: float = ...,
        X: int = ...,
        Y: int = ...,
        Z: int = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""

class SampleIndex:
    """Retrieve values from specific geometry elements"""
    def __init__(
        self,
        data_type: Any,
        domain: Any,
        clamp: bool,
        Geometry: Any = ...,
        Value: float = ...,
        Index: int = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""

class SampleNearest:
    """Find the element of a geometry closest to a position. Similar to the "Index of Nearest" node"""
    def __init__(
        self,
        domain: Any,
        Geometry: Any = ...,
        Sample_Position: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Index(self) -> int:
        """Index"""

class SampleNearestSurface:
    """Calculate the interpolated value of a mesh attribute on the closest point of its surface"""
    def __init__(
        self,
        data_type: Any,
        Mesh: Any = ...,
        Value: float = ...,
        Group_ID: int = ...,
        Sample_Position: Tuple[float, float, float] = ...,
        Sample_Group_ID: int = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""
    def Is_Valid(self) -> bool:
        """Is Valid"""

class SampleUVSurface:
    """Calculate the interpolated values of a mesh attribute at a UV coordinate"""
    def __init__(
        self,
        data_type: Any,
        Mesh: Any = ...,
        Value: float = ...,
        UV_Map: Tuple[float, float, float] = ...,
        Sample_UV: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Value(self) -> float:
        """Value"""
    def Is_Valid(self) -> bool:
        """Is Valid"""

class ScaleElements:
    """Scale groups of connected edges and faces"""
    def __init__(
        self,
        domain: Any,
        scale_mode: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Scale: float = ...,
        Center: Tuple[float, float, float] = ...,
        Axis: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class ScaleInstances:
    """Scale geometry instances in local or global space"""
    def __init__(
        self,
        Instances: Any = ...,
        Selection: bool = ...,
        Scale: Tuple[float, float, float] = ...,
        Center: Tuple[float, float, float] = ...,
        Local_Space: bool = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class SelfObject:
    """Retrieve the object that contains the geometry nodes modifier currently being executed"""
    def __init__(
        self,
    ) -> None: ...
    def Self_Object(self) -> Any:
        """Self Object"""

class SeparateComponents:
    """Split a geometry into a separate output for each type of data in the geometry"""
    def __init__(self, Geometry: Any = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""
    def Curve(self) -> Any:
        """Curve"""
    def Grease_Pencil(self) -> Any:
        """Grease Pencil"""
    def Point_Cloud(self) -> Any:
        """Point Cloud"""
    def Volume(self) -> Any:
        """Volume"""
    def Instances(self) -> Any:
        """Instances"""

class SeparateGeometry:
    """Split a geometry into two geometry outputs based on a selection"""
    def __init__(
        self, domain: Any, Geometry: Any = ..., Selection: bool = ...
    ) -> None: ...
    def Selection(self) -> Any:
        """Selection"""
    def Inverted(self) -> Any:
        """Inverted"""

class SetCurveHandlePositions:
    """Set the positions for the handles of Bézier curves"""
    def __init__(
        self,
        mode: Any,
        Curve: Any = ...,
        Selection: bool = ...,
        Position: Tuple[float, float, float] = ...,
        Offset: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class SetCurveNormal:
    """Set the evaluation mode for curve normals"""
    def __init__(
        self,
        mode: Any,
        Curve: Any = ...,
        Selection: bool = ...,
        Normal: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class SetCurveRadius:
    """Set the radius of the curve at each control point"""
    def __init__(
        self, Curve: Any = ..., Selection: bool = ..., Radius: float = ...
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class SetCurveTilt:
    """Set the tilt angle at each curve control point"""
    def __init__(
        self, Curve: Any = ..., Selection: bool = ..., Tilt: float = ...
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class SetGeometryName:
    """Set the name of a geometry for easier debugging"""
    def __init__(self, Geometry: Any = ..., Name: str = ...) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetID:
    """Set the id attribute on the input geometry, mainly used internally for randomizing"""
    def __init__(
        self, Geometry: Any = ..., Selection: bool = ..., ID: int = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetInstanceTransform:
    """Set the transformation matrix of every instance"""
    def __init__(
        self, Instances: Any = ..., Selection: bool = ..., Transform: Any = ...
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class SetMaterial:
    """Assign a material to geometry elements"""
    def __init__(
        self, Geometry: Any = ..., Selection: bool = ..., Material: Any = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetMaterialIndex:
    """Set the material index for each selected geometry element"""
    def __init__(
        self, Geometry: Any = ..., Selection: bool = ..., Material_Index: int = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetPointRadius:
    """Set the display size of point cloud points"""
    def __init__(
        self, Points: Any = ..., Selection: bool = ..., Radius: float = ...
    ) -> None: ...
    def Points(self) -> Any:
        """Points"""

class SetPosition:
    """Set the location of each point"""
    def __init__(
        self,
        Geometry: Any = ...,
        Selection: bool = ...,
        Position: Tuple[float, float, float] = ...,
        Offset: Tuple[float, float, float] = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetShadeSmooth:
    """Control the smoothness of mesh normals around each face by changing the "shade smooth" attribute"""
    def __init__(
        self,
        domain: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Shade_Smooth: bool = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetSplineCyclic:
    """Control whether each spline loops back on itself by changing the "cyclic" attribute"""
    def __init__(
        self, Geometry: Any = ..., Selection: bool = ..., Cyclic: bool = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SetSplineResolution:
    """Control how many evaluated points should be generated on every curve segment"""
    def __init__(
        self, Geometry: Any = ..., Selection: bool = ..., Resolution: int = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SimulationInput:
    """Input data for the simulation zone"""
    def __init__(
        self,
    ) -> None: ...
    def Delta_Time(self) -> float:
        """Delta Time"""

class SimulationOutput:
    """Output data from the simulation zone"""
    def __init__(
        self, active_index: int, active_item: Any, Skip: bool = ..., Geometry: Any = ...
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SortElements:
    """Rearrange geometry elements, changing their indices"""
    def __init__(
        self,
        domain: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Group_ID: int = ...,
        Sort_Weight: float = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class SplineLength:
    """Retrieve the total length of each spline, as a distance or as a number of points"""
    def __init__(
        self,
    ) -> None: ...
    def Length(self) -> float:
        """Length"""
    def Point_Count(self) -> int:
        """Point Count"""

class SplineParameter:
    """Retrieve how far along each spline a control point is"""
    def __init__(
        self,
    ) -> None: ...
    def Factor(self) -> float:
        """Factor"""
    def Length(self) -> float:
        """Length"""
    def Index(self) -> int:
        """Index"""

class SplitEdges:
    """Duplicate mesh edges and break connections with the surrounding faces"""
    def __init__(self, Mesh: Any = ..., Selection: bool = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class SplitToInstances:
    """Create separate geometries containing the elements from the same group"""
    def __init__(
        self,
        domain: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Group_ID: int = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""
    def Group_ID(self) -> int:
        """Group ID"""

class StoreNamedAttribute:
    """Store the result of a field on a geometry as an attribute with the specified name"""
    def __init__(
        self,
        data_type: Any,
        domain: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
        Name: str = ...,
        Value: float = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class StoreNamedGrid:
    """Store grid data in a volume geometry with the specified name"""
    def __init__(
        self, data_type: Any, Volume: Any = ..., Name: str = ..., Grid: float = ...
    ) -> None: ...
    def Volume(self) -> Any:
        """Volume"""

class StringJoin:
    """Combine any number of input strings"""
    def __init__(self, Delimiter: str = ..., Strings: str = ...) -> None: ...
    def String(self) -> str:
        """String"""

class StringToCurves:
    """Generate a paragraph of text with a specific font, using a curve instance to store each character"""
    def __init__(
        self,
        font: Any,
        overflow: Any,
        align_x: Any,
        align_y: Any,
        pivot_mode: Any,
        String: str = ...,
        Size: float = ...,
        Character_Spacing: float = ...,
        Word_Spacing: float = ...,
        Line_Spacing: float = ...,
        Text_Box_Width: float = ...,
        Text_Box_Height: float = ...,
    ) -> None: ...
    def Curve_Instances(self) -> Any:
        """Curve Instances"""
    def Remainder(self) -> str:
        """Remainder"""
    def Line(self) -> int:
        """Line"""
    def Pivot_Point(self) -> Tuple[float, float, float]:
        """Pivot Point"""

class SubdivideCurve:
    """Dividing each curve segment into a specified number of pieces"""
    def __init__(self, Curve: Any = ..., Cuts: int = ...) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class SubdivideMesh:
    """Divide mesh faces into smaller ones without changing the shape or volume, using linear interpolation to place the new vertices"""
    def __init__(self, Mesh: Any = ..., Level: int = ...) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class SubdivisionSurface:
    """Divide mesh faces to form a smooth surface, using the Catmull-Clark subdivision method"""
    def __init__(
        self,
        uv_smooth: Any,
        boundary_smooth: Any,
        Mesh: Any = ...,
        Level: int = ...,
        Edge_Crease: float = ...,
        Vertex_Crease: float = ...,
        Limit_Surface: bool = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class Switch:
    """Switch between two inputs"""
    def __init__(
        self,
        input_type: Any,
        Switch: bool = ...,
        on_False: Any = ...,
        on_True: Any = ...,
    ) -> None: ...
    def Output(self) -> Any:
        """Output"""

class Tool3DCursor:
    """The scene's 3D cursor location and rotation"""
    def __init__(
        self,
    ) -> None: ...
    def Location(self) -> Tuple[float, float, float]:
        """Location"""
    def Rotation(self) -> Any:
        """Rotation"""

class ToolActiveElement:
    """Active element indices of the edited geometry, for tool execution"""
    def __init__(self, domain: Any) -> None: ...
    def Index(self) -> int:
        """Index"""
    def Exists(self) -> bool:
        """Exists"""

class ToolFaceSet:
    """Each face's sculpt face set value"""
    def __init__(
        self,
    ) -> None: ...
    def Face_Set(self) -> int:
        """Face Set"""
    def Exists(self) -> bool:
        """Exists"""

class ToolMousePosition:
    """Retrieve the position of the mouse cursor"""
    def __init__(
        self,
    ) -> None: ...
    def Mouse_X(self) -> int:
        """Mouse X"""
    def Mouse_Y(self) -> int:
        """Mouse Y"""
    def Region_Width(self) -> int:
        """Region Width"""
    def Region_Height(self) -> int:
        """Region Height"""

class ToolSelection:
    """User selection of the edited geometry, for tool execution"""
    def __init__(
        self,
    ) -> None: ...
    def Boolean(self) -> bool:
        """Boolean"""
    def Float(self) -> float:
        """Float"""

class ToolSetFaceSet:
    """Set sculpt face set values for faces"""
    def __init__(
        self, Mesh: Any = ..., Selection: bool = ..., Face_Set: int = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class ToolSetSelection:
    """Set selection of the edited geometry, for tool execution"""
    def __init__(
        self,
        domain: Any,
        selection_type: Any,
        Geometry: Any = ...,
        Selection: bool = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class Transform:
    """Translate, rotate or scale the geometry"""
    def __init__(
        self,
        mode: Any,
        Geometry: Any = ...,
        Translation: Tuple[float, float, float] = ...,
        Rotation: Any = ...,
        Scale: Tuple[float, float, float] = ...,
        Transform: Any = ...,
    ) -> None: ...
    def Geometry(self) -> Any:
        """Geometry"""

class TranslateInstances:
    """Move top-level geometry instances in local or global space"""
    def __init__(
        self,
        Instances: Any = ...,
        Selection: bool = ...,
        Translation: Tuple[float, float, float] = ...,
        Local_Space: bool = ...,
    ) -> None: ...
    def Instances(self) -> Any:
        """Instances"""

class Triangulate:
    """Convert all faces in a mesh to triangular faces"""
    def __init__(
        self, quad_method: Any, ngon_method: Any, Mesh: Any = ..., Selection: bool = ...
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class TrimCurve:
    """Shorten curves by removing portions at the start or end"""
    def __init__(
        self,
        mode: Any,
        Curve: Any = ...,
        Selection: bool = ...,
        Start1: float = ...,
        End1: float = ...,
        Start2: float = ...,
        End2: float = ...,
    ) -> None: ...
    def Curve(self) -> Any:
        """Curve"""

class UVPackIslands:
    """Scale islands of a UV map and move them so they fill the UV space as much as possible"""
    def __init__(
        self,
        UV: Tuple[float, float, float] = ...,
        Selection: bool = ...,
        Margin: float = ...,
        Rotate: bool = ...,
    ) -> None: ...
    def UV(self) -> Tuple[float, float, float]:
        """UV"""

class UVUnwrap:
    """Generate a UV map based on seam edges"""
    def __init__(
        self,
        method: Any,
        Selection: bool = ...,
        Seam: bool = ...,
        Margin: float = ...,
        Fill_Holes: bool = ...,
    ) -> None: ...
    def UV(self) -> Tuple[float, float, float]:
        """UV"""

class VertexOfCorner:
    """Retrieve the vertex each face corner is attached to"""
    def __init__(self, Corner_Index: int = ...) -> None: ...
    def Vertex_Index(self) -> int:
        """Vertex Index"""

class Viewer:
    """Display the input data in the Spreadsheet Editor"""
    def __init__(
        self, data_type: Any, domain: Any, Geometry: Any = ..., Value: float = ...
    ) -> None: ...

class ViewportTransform:
    """Retrieve the view direction and location of the 3D viewport"""
    def __init__(
        self,
    ) -> None: ...
    def Projection(self) -> Any:
        """Projection"""
    def View(self) -> Any:
        """View"""
    def Is_Orthographic(self) -> bool:
        """Is Orthographic"""

class VolumeCube:
    """Generate a dense volume with a field that controls the density at each grid voxel based on its position"""
    def __init__(
        self,
        Density: float = ...,
        Background: float = ...,
        Min: Tuple[float, float, float] = ...,
        Max: Tuple[float, float, float] = ...,
        Resolution_X: int = ...,
        Resolution_Y: int = ...,
        Resolution_Z: int = ...,
    ) -> None: ...
    def Volume(self) -> Any:
        """Volume"""

class VolumeToMesh:
    """Generate a mesh on the "surface" of a volume"""
    def __init__(
        self,
        resolution_mode: Any,
        Volume: Any = ...,
        Voxel_Size: float = ...,
        Voxel_Amount: float = ...,
        Threshold: float = ...,
        Adaptivity: float = ...,
    ) -> None: ...
    def Mesh(self) -> Any:
        """Mesh"""

class Warning:
    """Create custom warnings in node groups"""
    def __init__(
        self, warning_type: Any, Show: bool = ..., Message: str = ...
    ) -> None: ...
    def Show(self) -> bool:
        """Show"""
