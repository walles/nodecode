# Generated from Blender 4.4.1 on 2025-04-21 16:26:06
from typing import Any, Tuple

class AddShader:
    """Add two Shaders together"""
    def __init__(self, Shader1: Any = ..., Shader2: Any = ...) -> None: ...
    def Shader(self) -> Any: """Shader"""

class AmbientOcclusion:
    """Compute how much the hemisphere above the shading point is occluded, for example to add weathering effects to corners.
Note: For Cycles, this may slow down renders significantly"""
    def __init__(self, samples: int, inside: bool, only_local: bool, Color: Tuple[float, float, float, float] = ..., Distance: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def AO(self) -> float: """AO"""

class Attribute:
    """Retrieve attributes attached to objects or geometry"""
    def __init__(self, attribute_type: Any, attribute_name: str) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Vector(self) -> Tuple[float, float, float]: """Vector"""
    def Fac(self) -> float: """Fac"""
    def Alpha(self) -> float: """Alpha"""

class Background:
    """Add background light emission.
Note: This node should only be used for the world surface output"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Strength: float = ..., Weight: float = ...) -> None: ...
    def Background(self) -> Any: """Background"""

class Bevel:
    """Generates normals with round corners.
Note: only supported in Cycles, and may slow down renders"""
    def __init__(self, samples: int, Radius: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Normal(self) -> Tuple[float, float, float]: """Normal"""

class Blackbody:
    """Convert a blackbody temperature to an RGB value"""
    def __init__(self, Temperature: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class BrightContrast:
    """Control the brightness and contrast of the input color"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Bright: float = ..., Contrast: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class BsdfAnisotropic:
    """Reflection with microfacet distribution, used for materials such as metal or mirrors"""
    def __init__(self, distribution: Any, Color: Tuple[float, float, float, float] = ..., Roughness: float = ..., Anisotropy: float = ..., Rotation: float = ..., Normal: Tuple[float, float, float] = ..., Tangent: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfDiffuse:
    """Lambertian and Oren-Nayar diffuse reflection"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Roughness: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfGlass:
    """Glass-like shader mixing refraction and reflection at grazing angles"""
    def __init__(self, distribution: Any, Color: Tuple[float, float, float, float] = ..., Roughness: float = ..., IOR: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfHair:
    """Reflection and transmission shaders optimized for hair rendering"""
    def __init__(self, component: Any, Color: Tuple[float, float, float, float] = ..., Offset: float = ..., RoughnessU: float = ..., RoughnessV: float = ..., Tangent: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfHairPrincipled:
    """Physically-based, easy-to-use shader for rendering hair and fur"""
    def __init__(self, model: Any, parametrization: Any, Color: Tuple[float, float, float, float] = ..., Melanin: float = ..., Melanin_Redness: float = ..., Tint: Tuple[float, float, float, float] = ..., Absorption_Coefficient: Tuple[float, float, float] = ..., Aspect_Ratio: float = ..., Roughness: float = ..., Radial_Roughness: float = ..., Coat: float = ..., IOR: float = ..., Offset: float = ..., Random_Color: float = ..., Random_Roughness: float = ..., Random: float = ..., Weight: float = ..., Reflection: float = ..., Transmission: float = ..., Secondary_Reflection: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfMetallic:
    """Metallic reflection with microfacet distribution, and metallic fresnel"""
    def __init__(self, distribution: Any, fresnel_type: Any, Base_Color: Tuple[float, float, float, float] = ..., Edge_Tint: Tuple[float, float, float, float] = ..., IOR: Tuple[float, float, float] = ..., Extinction: Tuple[float, float, float] = ..., Roughness: float = ..., Anisotropy: float = ..., Rotation: float = ..., Normal: Tuple[float, float, float] = ..., Tangent: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfPrincipled:
    """Physically-based, easy-to-use shader for rendering surface materials, based on the OpenPBR model"""
    def __init__(self, distribution: Any, subsurface_method: Any, Base_Color: Tuple[float, float, float, float] = ..., Metallic: float = ..., Roughness: float = ..., IOR: float = ..., Alpha: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ..., Diffuse_Roughness: float = ..., Subsurface_Weight: float = ..., Subsurface_Radius: Tuple[float, float, float] = ..., Subsurface_Scale: float = ..., Subsurface_IOR: float = ..., Subsurface_Anisotropy: float = ..., Specular_IOR_Level: float = ..., Specular_Tint: Tuple[float, float, float, float] = ..., Anisotropic: float = ..., Anisotropic_Rotation: float = ..., Tangent: Tuple[float, float, float] = ..., Transmission_Weight: float = ..., Coat_Weight: float = ..., Coat_Roughness: float = ..., Coat_IOR: float = ..., Coat_Tint: Tuple[float, float, float, float] = ..., Coat_Normal: Tuple[float, float, float] = ..., Sheen_Weight: float = ..., Sheen_Roughness: float = ..., Sheen_Tint: Tuple[float, float, float, float] = ..., Emission_Color: Tuple[float, float, float, float] = ..., Emission_Strength: float = ..., Thin_Film_Thickness: float = ..., Thin_Film_IOR: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfRayPortal:
    """Continue tracing from an arbitrary new position and in a new direction"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Position: Tuple[float, float, float] = ..., Direction: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfRefraction:
    """Glossy refraction with sharp or microfacet distribution, typically used for materials that transmit light"""
    def __init__(self, distribution: Any, Color: Tuple[float, float, float, float] = ..., Roughness: float = ..., IOR: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfSheen:
    """Reflection for materials such as cloth.
Typically mixed with other shaders (such as a Diffuse Shader) and is not particularly useful on its own"""
    def __init__(self, distribution: Any, Color: Tuple[float, float, float, float] = ..., Roughness: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfToon:
    """Diffuse and Glossy shaders with cartoon light effects"""
    def __init__(self, component: Any, Color: Tuple[float, float, float, float] = ..., Size: float = ..., Smooth: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfTranslucent:
    """Lambertian diffuse transmission"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class BsdfTransparent:
    """Transparency without refraction, passing straight through the surface as if there were no geometry"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class Bump:
    """Generate a perturbed normal from a height texture for bump mapping. Typically used for faking highly detailed surfaces"""
    def __init__(self, invert: bool, Strength: float = ..., Distance: float = ..., Filter_Width: float = ..., Height: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Normal(self) -> Tuple[float, float, float]: """Normal"""

class CameraData:
    """Retrieve information about the camera and how it relates to the current shading point's position"""
    def __init__(self, ) -> None: ...
    def View_Vector(self) -> Tuple[float, float, float]: """View Vector"""
    def View_Z_Depth(self) -> float: """View Z Depth"""
    def View_Distance(self) -> float: """View Distance"""

class Clamp:
    """Clamp a value between a minimum and a maximum"""
    def __init__(self, clamp_type: Any, Value: float = ..., Min: float = ..., Max: float = ...) -> None: ...
    def Result(self) -> float: """Result"""

class CombineColor:
    """Create a color from individual components using multiple models"""
    def __init__(self, mode: Any, Red: float = ..., Green: float = ..., Blue: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class CombineHSV:
    """Deprecated"""
    def __init__(self, H: float = ..., S: float = ..., V: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class CombineRGB:
    """Deprecated"""
    def __init__(self, R: float = ..., G: float = ..., B: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombineXYZ:
    """Create a vector from X, Y, and Z components"""
    def __init__(self, X: float = ..., Y: float = ..., Z: float = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class Displacement:
    """Displace the surface along the surface normal"""
    def __init__(self, space: Any, Height: float = ..., Midlevel: float = ..., Scale: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Displacement(self) -> Tuple[float, float, float]: """Displacement"""

class EeveeSpecular:
    """Similar to the Principled BSDF node but uses the specular workflow instead of metallic, which functions by specifying the facing (along normal) reflection color. Energy is not conserved, so the result may not be physically accurate"""
    def __init__(self, Base_Color: Tuple[float, float, float, float] = ..., Specular: Tuple[float, float, float, float] = ..., Roughness: float = ..., Emissive_Color: Tuple[float, float, float, float] = ..., Transparency: float = ..., Normal: Tuple[float, float, float] = ..., Clear_Coat: float = ..., Clear_Coat_Roughness: float = ..., Clear_Coat_Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSDF(self) -> Any: """BSDF"""

class Emission:
    """Lambertian emission shader"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Strength: float = ..., Weight: float = ...) -> None: ...
    def Emission(self) -> Any: """Emission"""

class FloatCurve:
    """Map an input float to a curve and outputs a float value"""
    def __init__(self, Factor: float = ..., Value: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class Fresnel:
    """Produce a blending factor depending on the angle between the surface normal and the view direction using Fresnel equations.
Typically used for mixing reflections at grazing angles"""
    def __init__(self, IOR: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Fac(self) -> float: """Fac"""

class Gamma:
    """Apply a gamma correction"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Gamma: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class Group:
    """Group"""
    def __init__(self, node_tree: Any) -> None: ...

class HairInfo:
    """Retrieve hair curve information"""
    def __init__(self, ) -> None: ...
    def Is_Strand(self) -> float: """Is Strand"""
    def Intercept(self) -> float: """Intercept"""
    def Length(self) -> float: """Length"""
    def Thickness(self) -> float: """Thickness"""
    def Tangent_Normal(self) -> Tuple[float, float, float]: """Tangent Normal"""
    def Random(self) -> float: """Random"""

class Holdout:
    """Create a "hole" in the image with zero alpha transparency, which is useful for compositing.
Note: the holdout shader can only create alpha when transparency is enabled in the film settings"""
    def __init__(self, Weight: float = ...) -> None: ...
    def Holdout(self) -> Any: """Holdout"""

class HueSaturation:
    """Apply a color transformation in the HSV color model"""
    def __init__(self, Hue: float = ..., Saturation: float = ..., Value: float = ..., Fac: float = ..., Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class Invert:
    """Invert a color, producing a negative"""
    def __init__(self, Fac: float = ..., Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class LayerWeight:
    """Produce a blending factor depending on the angle between the surface normal and the view direction.
Typically used for layering shaders with the Mix Shader node"""
    def __init__(self, Blend: float = ..., Normal: Tuple[float, float, float] = ...) -> None: ...
    def Fresnel(self) -> float: """Fresnel"""
    def Facing(self) -> float: """Facing"""

class LightFalloff:
    """Manipulate how light intensity decreases over distance. Typically used for non-physically-based effects; in reality light always falls off quadratically"""
    def __init__(self, Strength: float = ..., Smooth: float = ...) -> None: ...
    def Quadratic(self) -> float: """Quadratic"""
    def Linear(self) -> float: """Linear"""
    def Constant(self) -> float: """Constant"""

class LightPath:
    """Retrieve the type of incoming ray for which the shader is being executed.
Typically used for non-physically-based tricks"""
    def __init__(self, ) -> None: ...
    def Is_Camera_Ray(self) -> float: """Is Camera Ray"""
    def Is_Shadow_Ray(self) -> float: """Is Shadow Ray"""
    def Is_Diffuse_Ray(self) -> float: """Is Diffuse Ray"""
    def Is_Glossy_Ray(self) -> float: """Is Glossy Ray"""
    def Is_Singular_Ray(self) -> float: """Is Singular Ray"""
    def Is_Reflection_Ray(self) -> float: """Is Reflection Ray"""
    def Is_Transmission_Ray(self) -> float: """Is Transmission Ray"""
    def Ray_Length(self) -> float: """Ray Length"""
    def Ray_Depth(self) -> float: """Ray Depth"""
    def Diffuse_Depth(self) -> float: """Diffuse Depth"""
    def Glossy_Depth(self) -> float: """Glossy Depth"""
    def Transparent_Depth(self) -> float: """Transparent Depth"""
    def Transmission_Depth(self) -> float: """Transmission Depth"""

class MapRange:
    """Remap a value from a range to a target range"""
    def __init__(self, clamp: bool, interpolation_type: Any, data_type: Any, Value: float = ..., From_Min1: float = ..., From_Max1: float = ..., To_Min1: float = ..., To_Max1: float = ..., Steps1: float = ..., Vector: Tuple[float, float, float] = ..., From_Min2: Tuple[float, float, float] = ..., From_Max2: Tuple[float, float, float] = ..., To_Min2: Tuple[float, float, float] = ..., To_Max2: Tuple[float, float, float] = ..., Steps2: Tuple[float, float, float] = ...) -> None: ...
    def Result(self) -> float: """Result"""
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class Mapping:
    """Transform the input vector by applying translation, rotation, and scale"""
    def __init__(self, vector_type: Any, Vector: Tuple[float, float, float] = ..., Location: Tuple[float, float, float] = ..., Rotation: Tuple[float, float, float] = ..., Scale: Tuple[float, float, float] = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class Math:
    """Perform math operations"""
    def __init__(self, operation: Any, use_clamp: bool, Value1: float = ..., Value2: float = ..., Value3: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class Mix:
    """Mix values by a factor"""
    def __init__(self, data_type: Any, factor_mode: Any, blend_type: Any, clamp_factor: bool, clamp_result: bool, Factor1: float = ..., Factor2: Tuple[float, float, float] = ..., A1: float = ..., B1: float = ..., A2: Tuple[float, float, float] = ..., B2: Tuple[float, float, float] = ..., A3: Tuple[float, float, float, float] = ..., B3: Tuple[float, float, float, float] = ..., A4: Any = ..., B4: Any = ...) -> None: ...
    def Result1(self) -> float: """Result"""
    def Result2(self) -> Tuple[float, float, float]: """Result"""
    def Result3(self) -> Tuple[float, float, float, float]: """Result"""
    def Result4(self) -> Any: """Result"""

class MixRGB:
    """Mix two input colors"""
    def __init__(self, blend_type: Any, use_alpha: bool, use_clamp: bool, Fac: float = ..., Color1: Tuple[float, float, float, float] = ..., Color2: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class MixShader:
    """Mix two shaders together. Typically used for material layering"""
    def __init__(self, Fac: float = ..., Shader1: Any = ..., Shader2: Any = ...) -> None: ...
    def Shader(self) -> Any: """Shader"""

class NewGeometry:
    """Retrieve geometric information about the current shading point"""
    def __init__(self, ) -> None: ...
    def Position(self) -> Tuple[float, float, float]: """Position"""
    def Normal(self) -> Tuple[float, float, float]: """Normal"""
    def Tangent(self) -> Tuple[float, float, float]: """Tangent"""
    def True_Normal(self) -> Tuple[float, float, float]: """True Normal"""
    def Incoming(self) -> Tuple[float, float, float]: """Incoming"""
    def Parametric(self) -> Tuple[float, float, float]: """Parametric"""
    def Backfacing(self) -> float: """Backfacing"""
    def Pointiness(self) -> float: """Pointiness"""
    def Random_Per_Island(self) -> float: """Random Per Island"""

class Normal:
    """Generate a normal vector and a dot product"""
    def __init__(self, Normal: Tuple[float, float, float] = ...) -> None: ...
    def Normal(self) -> Tuple[float, float, float]: """Normal"""
    def Dot(self) -> float: """Dot"""

class NormalMap:
    """Generate a perturbed normal from an RGB normal map image. Typically used for faking highly detailed surfaces"""
    def __init__(self, space: Any, uv_map: str, Strength: float = ..., Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Normal(self) -> Tuple[float, float, float]: """Normal"""

class ObjectInfo:
    """Retrieve information about the object instance"""
    def __init__(self, ) -> None: ...
    def Location(self) -> Tuple[float, float, float]: """Location"""
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Alpha(self) -> float: """Alpha"""
    def Object_Index(self) -> float: """Object Index"""
    def Material_Index(self) -> float: """Material Index"""
    def Random(self) -> float: """Random"""

class OutputAOV:
    """Arbitrary Output Variables.
Provide custom render passes for arbitrary shader node outputs"""
    def __init__(self, aov_name: str, Color: Tuple[float, float, float, float] = ..., Value: float = ...) -> None: ...

class OutputLight:
    """Output light information to a light object"""
    def __init__(self, is_active_output: bool, target: Any, Surface: Any = ...) -> None: ...

class OutputLineStyle:
    """Line Style Output"""
    def __init__(self, is_active_output: bool, target: Any, blend_type: Any, use_alpha: bool, use_clamp: bool, Color: Tuple[float, float, float, float] = ..., Color_Fac: float = ..., Alpha: float = ..., Alpha_Fac: float = ...) -> None: ...

class OutputMaterial:
    """Output surface material information for use in rendering"""
    def __init__(self, is_active_output: bool, target: Any, Surface: Any = ..., Volume: Any = ..., Displacement: Tuple[float, float, float] = ..., Thickness: float = ...) -> None: ...

class OutputWorld:
    """Output light color information to the scene's World"""
    def __init__(self, is_active_output: bool, target: Any, Surface: Any = ..., Volume: Any = ...) -> None: ...

class ParticleInfo:
    """Retrieve the data of the particle that spawned the object instance, for example to give variation to multiple instances of an object"""
    def __init__(self, ) -> None: ...
    def Index(self) -> float: """Index"""
    def Random(self) -> float: """Random"""
    def Age(self) -> float: """Age"""
    def Lifetime(self) -> float: """Lifetime"""
    def Location(self) -> Tuple[float, float, float]: """Location"""
    def Size(self) -> float: """Size"""
    def Velocity(self) -> Tuple[float, float, float]: """Velocity"""
    def Angular_Velocity(self) -> Tuple[float, float, float]: """Angular Velocity"""

class PointInfo:
    """Retrieve information about points in a point cloud"""
    def __init__(self, ) -> None: ...
    def Position(self) -> Tuple[float, float, float]: """Position"""
    def Radius(self) -> float: """Radius"""
    def Random(self) -> float: """Random"""

class RGB:
    """A color picker"""
    def __init__(self, ) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class RGBCurve:
    """Apply color corrections for each color channel"""
    def __init__(self, Fac: float = ..., Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class RGBToBW:
    """Convert a color's luminance to a grayscale value"""
    def __init__(self, Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Val(self) -> float: """Val"""

class Script:
    """Generate an OSL shader from a file or text data-block.
Note: OSL shaders are not supported on all GPU backends"""
    def __init__(self, script: Any, filepath: str, mode: Any, use_auto_update: bool, bytecode: str, bytecode_hash: str) -> None: ...

class SeparateColor:
    """Split a color into its individual components using multiple models"""
    def __init__(self, mode: Any, Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Red(self) -> float: """Red"""
    def Green(self) -> float: """Green"""
    def Blue(self) -> float: """Blue"""

class SeparateHSV:
    """Deprecated"""
    def __init__(self, Color: Tuple[float, float, float, float] = ...) -> None: ...
    def H(self) -> float: """H"""
    def S(self) -> float: """S"""
    def V(self) -> float: """V"""

class SeparateRGB:
    """Deprecated"""
    def __init__(self, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def R(self) -> float: """R"""
    def G(self) -> float: """G"""
    def B(self) -> float: """B"""

class SeparateXYZ:
    """Split a vector into its X, Y, and Z components"""
    def __init__(self, Vector: Tuple[float, float, float] = ...) -> None: ...
    def X(self) -> float: """X"""
    def Y(self) -> float: """Y"""
    def Z(self) -> float: """Z"""

class ShaderToRGB:
    """Convert rendering effect (such as light and shadow) to color. Typically used for non-photorealistic rendering, to apply additional effects on the output of BSDFs.
Note: only supported in EEVEE"""
    def __init__(self, Shader: Any = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Alpha(self) -> float: """Alpha"""

class Squeeze:
    """Deprecated"""
    def __init__(self, Value: float = ..., Width: float = ..., Center: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class SubsurfaceScattering:
    """Subsurface multiple scattering shader to simulate light entering the surface and bouncing internally.
Typically used for materials such as skin, wax, marble or milk"""
    def __init__(self, falloff: Any, Color: Tuple[float, float, float, float] = ..., Scale: float = ..., Radius: Tuple[float, float, float] = ..., IOR: float = ..., Roughness: float = ..., Anisotropy: float = ..., Normal: Tuple[float, float, float] = ..., Weight: float = ...) -> None: ...
    def BSSRDF(self) -> Any: """BSSRDF"""

class Tangent:
    """Generate a tangent direction for the Anisotropic BSDF"""
    def __init__(self, direction_type: Any, axis: Any, uv_map: str) -> None: ...
    def Tangent(self) -> Tuple[float, float, float]: """Tangent"""

class TexBrick:
    """Generate a procedural texture producing bricks"""
    def __init__(self, offset_frequency: int, squash_frequency: int, offset: Any, squash: Any, Vector: Tuple[float, float, float] = ..., Color1: Tuple[float, float, float, float] = ..., Color2: Tuple[float, float, float, float] = ..., Mortar: Tuple[float, float, float, float] = ..., Scale: float = ..., Mortar_Size: float = ..., Mortar_Smooth: float = ..., Bias: float = ..., Brick_Width: float = ..., Row_Height: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Fac(self) -> float: """Fac"""

class TexChecker:
    """Generate a checkerboard texture"""
    def __init__(self, Vector: Tuple[float, float, float] = ..., Color1: Tuple[float, float, float, float] = ..., Color2: Tuple[float, float, float, float] = ..., Scale: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Fac(self) -> float: """Fac"""

class TexCoord:
    """Retrieve multiple types of texture coordinates.
Typically used as inputs for texture nodes"""
    def __init__(self, object: Any, from_instancer: bool) -> None: ...
    def Generated(self) -> Tuple[float, float, float]: """Generated"""
    def Normal(self) -> Tuple[float, float, float]: """Normal"""
    def UV(self) -> Tuple[float, float, float]: """UV"""
    def Object(self) -> Tuple[float, float, float]: """Object"""
    def Camera(self) -> Tuple[float, float, float]: """Camera"""
    def Window(self) -> Tuple[float, float, float]: """Window"""
    def Reflection(self) -> Tuple[float, float, float]: """Reflection"""

class TexEnvironment:
    """Sample an image file as an environment texture. Typically used to light the scene with the background node"""
    def __init__(self, image: Any, projection: Any, interpolation: Any, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class TexGabor:
    """Generate Gabor noise"""
    def __init__(self, gabor_type: Any, Vector: Tuple[float, float, float] = ..., Scale: float = ..., Frequency: float = ..., Anisotropy: float = ..., Orientation1: float = ..., Orientation2: Tuple[float, float, float] = ...) -> None: ...
    def Value(self) -> float: """Value"""
    def Phase(self) -> float: """Phase"""
    def Intensity(self) -> float: """Intensity"""

class TexGradient:
    """Generate interpolated color and intensity values based on the input vector"""
    def __init__(self, gradient_type: Any, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Fac(self) -> float: """Fac"""

class TexIES:
    """Match real world lights with IES files, which store the directional intensity distribution of light sources"""
    def __init__(self, ies: Any, filepath: str, mode: Any, Vector: Tuple[float, float, float] = ..., Strength: float = ...) -> None: ...
    def Fac(self) -> float: """Fac"""

class TexImage:
    """Sample an image file as a texture"""
    def __init__(self, image: Any, projection: Any, interpolation: Any, projection_blend: Any, extension: Any, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Alpha(self) -> float: """Alpha"""

class TexMagic:
    """Generate a psychedelic color texture"""
    def __init__(self, turbulence_depth: int, Vector: Tuple[float, float, float] = ..., Scale: float = ..., Distortion: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Fac(self) -> float: """Fac"""

class TexNoise:
    """Generate fractal Perlin noise"""
    def __init__(self, noise_dimensions: Any, noise_type: Any, normalize: bool, Vector: Tuple[float, float, float] = ..., W: float = ..., Scale: float = ..., Detail: float = ..., Roughness: float = ..., Lacunarity: float = ..., Offset: float = ..., Gain: float = ..., Distortion: float = ...) -> None: ...
    def Fac(self) -> float: """Fac"""
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class TexPointDensity:
    """Generate a volumetric point for each particle or vertex of another object"""
    def __init__(self, object: Any, point_source: Any, particle_system: Any, resolution: int, radius: Any, space: Any, interpolation: Any, particle_color_source: Any, vertex_color_source: Any, vertex_attribute_name: str, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Density(self) -> float: """Density"""

class TexSky:
    """Generate a procedural sky texture"""
    def __init__(self, sky_type: Any, sun_direction: Any, turbidity: Any, ground_albedo: Any, sun_disc: bool, sun_size: Any, sun_intensity: Any, sun_elevation: Any, sun_rotation: Any, altitude: Any, air_density: Any, dust_density: Any, ozone_density: Any, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class TexVoronoi:
    """Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells"""
    def __init__(self, voronoi_dimensions: Any, distance: Any, feature: Any, normalize: bool, Vector: Tuple[float, float, float] = ..., W: float = ..., Scale: float = ..., Detail: float = ..., Roughness: float = ..., Lacunarity: float = ..., Smoothness: float = ..., Exponent: float = ..., Randomness: float = ...) -> None: ...
    def Distance(self) -> float: """Distance"""
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Position(self) -> Tuple[float, float, float]: """Position"""
    def W(self) -> float: """W"""
    def Radius(self) -> float: """Radius"""

class TexWave:
    """Generate procedural bands or rings with noise"""
    def __init__(self, wave_type: Any, bands_direction: Any, rings_direction: Any, wave_profile: Any, Vector: Tuple[float, float, float] = ..., Scale: float = ..., Distortion: float = ..., Detail: float = ..., Detail_Scale: float = ..., Detail_Roughness: float = ..., Phase_Offset: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Fac(self) -> float: """Fac"""

class TexWhiteNoise:
    """Return a random value or color based on an input seed"""
    def __init__(self, noise_dimensions: Any, Vector: Tuple[float, float, float] = ..., W: float = ...) -> None: ...
    def Value(self) -> float: """Value"""
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class UVAlongStroke:
    """UV Along Stroke"""
    def __init__(self, use_tips: bool) -> None: ...
    def UV(self) -> Tuple[float, float, float]: """UV"""

class UVMap:
    """Retrieve a UV map from the geometry, or the default fallback if none is specified"""
    def __init__(self, from_instancer: bool, uv_map: str) -> None: ...
    def UV(self) -> Tuple[float, float, float]: """UV"""

class ValToRGB:
    """Map values to colors with the use of a gradient"""
    def __init__(self, Fac: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Alpha(self) -> float: """Alpha"""

class Value:
    """Input numerical values to other nodes in the tree"""
    def __init__(self, ) -> None: ...
    def Value(self) -> float: """Value"""

class VectorCurve:
    """Map input vector components with curves"""
    def __init__(self, Fac: float = ..., Vector: Tuple[float, float, float] = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class VectorDisplacement:
    """Displace the surface along an arbitrary direction"""
    def __init__(self, space: Any, Vector: Tuple[float, float, float, float] = ..., Midlevel: float = ..., Scale: float = ...) -> None: ...
    def Displacement(self) -> Tuple[float, float, float]: """Displacement"""

class VectorMath:
    """Perform vector math operation"""
    def __init__(self, operation: Any, Vector1: Tuple[float, float, float] = ..., Vector2: Tuple[float, float, float] = ..., Vector3: Tuple[float, float, float] = ..., Scale: float = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""
    def Value(self) -> float: """Value"""

class VectorRotate:
    """Rotate a vector around a pivot point (center)"""
    def __init__(self, rotation_type: Any, invert: bool, Vector: Tuple[float, float, float] = ..., Center: Tuple[float, float, float] = ..., Axis: Tuple[float, float, float] = ..., Angle: float = ..., Rotation: Tuple[float, float, float] = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class VectorTransform:
    """Convert a vector, point, or normal between world, camera, and object coordinate space"""
    def __init__(self, vector_type: Any, convert_from: Any, convert_to: Any, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class VertexColor:
    """Retrieve a color attribute, or the default fallback if none is specified"""
    def __init__(self, layer_name: str) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Alpha(self) -> float: """Alpha"""

class VolumeAbsorption:
    """Absorb light as it passes through the volume"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Density: float = ..., Weight: float = ...) -> None: ...
    def Volume(self) -> Any: """Volume"""

class VolumeInfo:
    """Read volume data attributes from volume grids"""
    def __init__(self, ) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""
    def Density(self) -> float: """Density"""
    def Flame(self) -> float: """Flame"""
    def Temperature(self) -> float: """Temperature"""

class VolumePrincipled:
    """Combine all volume shading components into a single easy to use node"""
    def __init__(self, Color: Tuple[float, float, float, float] = ..., Color_Attribute: str = ..., Density: float = ..., Density_Attribute: str = ..., Anisotropy: float = ..., Absorption_Color: Tuple[float, float, float, float] = ..., Emission_Strength: float = ..., Emission_Color: Tuple[float, float, float, float] = ..., Blackbody_Intensity: float = ..., Blackbody_Tint: Tuple[float, float, float, float] = ..., Temperature: float = ..., Temperature_Attribute: str = ..., Weight: float = ...) -> None: ...
    def Volume(self) -> Any: """Volume"""

class VolumeScatter:
    """Scatter light as it passes through the volume, often used to add fog to a scene"""
    def __init__(self, phase: Any, Color: Tuple[float, float, float, float] = ..., Density: float = ..., Anisotropy: float = ..., IOR: float = ..., Backscatter: float = ..., Alpha: float = ..., Diameter: float = ..., Weight: float = ...) -> None: ...
    def Volume(self) -> Any: """Volume"""

class Wavelength:
    """Convert a wavelength value to an RGB value"""
    def __init__(self, Wavelength: float = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class Wireframe:
    """Retrieve the edges of an object as it appears to Cycles.
Note: as meshes are triangulated before being processed by Cycles, topology will always appear triangulated"""
    def __init__(self, use_pixel_size: bool, Size: float = ...) -> None: ...
    def Fac(self) -> float: """Fac"""

