# Generated from Blender 4.4.1 on 2025-04-21 16:52:34
from typing import Any, Tuple

class AlphaOver:
    """Overlay a foreground image onto a background image"""
    def __init__(self, use_premultiply: bool, premul: Any, Fac: float = ..., Image1: Tuple[float, float, float, float] = ..., Image2: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class AntiAliasing:
    """Smooth away jagged edges"""
    def __init__(self, threshold: Any, contrast_limit: Any, corner_rounding: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Bilateralblur:
    """Adaptively blur image, while retaining sharp edges"""
    def __init__(self, iterations: int, sigma_color: Any, sigma_space: Any, Image: Tuple[float, float, float, float] = ..., Determinator: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Blur:
    """Blur an image, using several blur modes"""
    def __init__(self, use_variable_size: bool, use_extended_bounds: bool, size_x: int, size_y: int, use_relative: bool, aspect_correction: Any, factor: Any, factor_x: Any, factor_y: Any, filter_type: Any, use_bokeh: bool, use_gamma_correction: bool, Image: Tuple[float, float, float, float] = ..., Size: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class BokehBlur:
    """Generate a bokeh type blur similar to Defocus. Unlike defocus an in-focus region is defined in the compositor"""
    def __init__(self, use_variable_size: bool, use_extended_bounds: bool, blur_max: Any, Image: Tuple[float, float, float, float] = ..., Bokeh: Tuple[float, float, float, float] = ..., Size: float = ..., Bounding_box: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class BokehImage:
    """Generate image with bokeh shape for use with the Bokeh Blur filter node"""
    def __init__(self, angle: Any, flaps: int, rounding: Any, catadioptric: Any, shift: Any) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class BoxMask:
    """Create rectangular mask suitable for use as a simple matte"""
    def __init__(self, mask_type: Any, x: Any, y: Any, mask_width: Any, mask_height: Any, rotation: Any, Mask: float = ..., Value: float = ...) -> None: ...
    def Mask(self) -> float: """Mask"""

class BrightContrast:
    """Adjust brightness and contrast"""
    def __init__(self, use_premultiply: bool, Image: Tuple[float, float, float, float] = ..., Bright: float = ..., Contrast: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class ChannelMatte:
    """Create matte based on differences in color channels"""
    def __init__(self, color_space: Any, matte_channel: Any, limit_method: Any, limit_channel: Any, limit_max: Any, limit_min: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class ChromaMatte:
    """Create matte based on chroma values"""
    def __init__(self, tolerance: Any, threshold: Any, lift: Any, gain: Any, shadow_adjust: Any, Image: Tuple[float, float, float, float] = ..., Key_Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class ColorBalance:
    """Adjust color and values"""
    def __init__(self, correction_method: Any, lift: Any, gamma: Any, gain: Any, offset: Any, power: Any, slope: Any, offset_basis: Any, input_temperature: Any, input_tint: Any, input_whitepoint: Any, output_temperature: Any, output_tint: Any, output_whitepoint: Any, Fac: float = ..., Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class ColorCorrection:
    """Adjust the color of an image, separately in several tonal ranges (highlights, midtones and shadows)"""
    def __init__(self, red: bool, green: bool, blue: bool, midtones_start: Any, midtones_end: Any, master_saturation: Any, master_contrast: Any, master_gamma: Any, master_gain: Any, master_lift: Any, shadows_saturation: Any, shadows_contrast: Any, shadows_gamma: Any, shadows_gain: Any, shadows_lift: Any, midtones_saturation: Any, midtones_contrast: Any, midtones_gamma: Any, midtones_gain: Any, midtones_lift: Any, highlights_saturation: Any, highlights_contrast: Any, highlights_gamma: Any, highlights_gain: Any, highlights_lift: Any, Image: Tuple[float, float, float, float] = ..., Mask: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class ColorMatte:
    """Create matte using a given color, for green or blue screen footage"""
    def __init__(self, color_hue: Any, color_saturation: Any, color_value: Any, Image: Tuple[float, float, float, float] = ..., Key_Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class ColorSpill:
    """Remove colors from a blue or green screen, by reducing one RGB channel compared to the others"""
    def __init__(self, channel: Any, limit_method: Any, limit_channel: Any, ratio: Any, use_unspill: bool, unspill_red: Any, unspill_green: Any, unspill_blue: Any, Image: Tuple[float, float, float, float] = ..., Fac: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombHSVA:
    """Deprecated"""
    def __init__(self, H: float = ..., S: float = ..., V: float = ..., A: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombRGBA:
    """Deprecated"""
    def __init__(self, R: float = ..., G: float = ..., B: float = ..., A: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombYCCA:
    """Deprecated"""
    def __init__(self, mode: Any, Y: float = ..., Cb: float = ..., Cr: float = ..., A: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombYUVA:
    """Deprecated"""
    def __init__(self, Y: float = ..., U: float = ..., V: float = ..., A: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombineColor:
    """Combine an image from its composite color channels"""
    def __init__(self, mode: Any, ycc_mode: Any, Red: float = ..., Green: float = ..., Blue: float = ..., Alpha: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CombineXYZ:
    """Combine a vector from its individual components"""
    def __init__(self, X: float = ..., Y: float = ..., Z: float = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class Composite:
    """Final render output"""
    def __init__(self, use_alpha: bool, Image: Tuple[float, float, float, float] = ..., Alpha: float = ...) -> None: ...

class ConvertColorSpace:
    """Convert between color spaces"""
    def __init__(self, from_color_space: Any, to_color_space: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CornerPin:
    """Plane warp transformation using explicit corner values"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Upper_Left: Tuple[float, float, float] = ..., Upper_Right: Tuple[float, float, float] = ..., Lower_Left: Tuple[float, float, float] = ..., Lower_Right: Tuple[float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Plane(self) -> float: """Plane"""

class Crop:
    """Crops image to a smaller region, either making the cropped area transparent or resizing the image"""
    def __init__(self, use_crop_size: bool, relative: bool, min_x: int, max_x: int, min_y: int, max_y: int, rel_min_x: Any, rel_max_x: Any, rel_min_y: Any, rel_max_y: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Cryptomatte:
    """Deprecated. Use Cryptomatte Node instead"""
    def __init__(self, matte_id: str, add: Any, remove: Any, Image: Tuple[float, float, float, float] = ..., Crypto_00: Tuple[float, float, float, float] = ..., Crypto_01: Tuple[float, float, float, float] = ..., Crypto_02: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""
    def Pick(self) -> Tuple[float, float, float, float]: """Pick"""

class CryptomatteV2:
    """Generate matte for individual objects and materials using Cryptomatte render passes"""
    def __init__(self, source: Any, scene: Any, image: Any, matte_id: str, add: Any, remove: Any, layer_name: Any, frame_duration: int, frame_start: int, frame_offset: int, use_cyclic: bool, use_auto_refresh: bool, layer: Any, view: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""
    def Pick(self) -> Tuple[float, float, float, float]: """Pick"""

class CurveRGB:
    """Perform level adjustments on each color channel of an image"""
    def __init__(self, Fac: float = ..., Image: Tuple[float, float, float, float] = ..., Black_Level: Tuple[float, float, float, float] = ..., White_Level: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class CurveVec:
    """Map input vector components with curves"""
    def __init__(self, Vector: Tuple[float, float, float] = ...) -> None: ...
    def Vector(self) -> Tuple[float, float, float]: """Vector"""

class DBlur:
    """Blur an image along a direction"""
    def __init__(self, iterations: int, center_x: Any, center_y: Any, distance: Any, angle: Any, spin: Any, zoom: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Defocus:
    """Apply depth of field in 2D, using a Z depth map or mask"""
    def __init__(self, scene: Any, bokeh: Any, angle: Any, use_gamma_correction: bool, f_stop: Any, blur_max: Any, threshold: Any, use_preview: bool, use_zbuffer: bool, z_scale: Any, Image: Tuple[float, float, float, float] = ..., Z: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Denoise:
    """Denoise renders from Cycles and other ray tracing renderers"""
    def __init__(self, use_hdr: bool, prefilter: Any, quality: Any, Image: Tuple[float, float, float, float] = ..., Normal: Tuple[float, float, float] = ..., Albedo: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Despeckle:
    """Smooth areas of an image in which noise is noticeable, while leaving complex areas untouched"""
    def __init__(self, threshold: Any, threshold_neighbor: Any, Fac: float = ..., Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class DiffMatte:
    """Produce a matte that isolates foreground content by comparing it with a reference background image"""
    def __init__(self, tolerance: Any, falloff: Any, Image_1: Tuple[float, float, float, float] = ..., Image_2: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class DilateErode:
    """Expand and shrink masks"""
    def __init__(self, mode: Any, distance: int, edge: Any, falloff: Any, Mask: float = ...) -> None: ...
    def Mask(self) -> float: """Mask"""

class Displace:
    """Displace pixel position using an offset vector"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Vector: Tuple[float, float, float] = ..., X_Scale: float = ..., Y_Scale: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class DistanceMatte:
    """Create matte based on 3D distance between colors"""
    def __init__(self, channel: Any, tolerance: Any, falloff: Any, Image: Tuple[float, float, float, float] = ..., Key_Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class DoubleEdgeMask:
    """Create a gradient between two masks"""
    def __init__(self, inner_mode: Any, edge_mode: Any, Inner_Mask: float = ..., Outer_Mask: float = ...) -> None: ...
    def Mask(self) -> float: """Mask"""

class EllipseMask:
    """Create elliptical mask suitable for use as a simple matte or vignette mask"""
    def __init__(self, mask_type: Any, x: Any, y: Any, mask_width: Any, mask_height: Any, rotation: Any, Mask: float = ..., Value: float = ...) -> None: ...
    def Mask(self) -> float: """Mask"""

class Exposure:
    """Adjust brightness using a camera exposure parameter"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Exposure: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Filter:
    """Apply common image enhancement filters"""
    def __init__(self, filter_type: Any, Fac: float = ..., Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Flip:
    """Flip an image along a defined axis"""
    def __init__(self, axis: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Gamma:
    """Apply gamma correction"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Gamma: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Glare:
    """Add lens flares, fog and glows around bright parts of the image"""
    def __init__(self, glare_type: Any, quality: Any, iterations: int, color_modulation: Any, mix: Any, threshold: Any, streaks: int, angle_offset: Any, fade: Any, use_rotate_45: bool, size: int, Image: Tuple[float, float, float, float] = ..., Threshold: float = ..., Smoothness: float = ..., Maximum: float = ..., Strength: float = ..., Saturation: float = ..., Tint: Tuple[float, float, float, float] = ..., Size: float = ..., Streaks: int = ..., Streaks_Angle: float = ..., Iterations: int = ..., Fade: float = ..., Color_Modulation: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Glare(self) -> Tuple[float, float, float, float]: """Glare"""
    def Highlights(self) -> Tuple[float, float, float, float]: """Highlights"""

class Group:
    """Group"""
    def __init__(self, node_tree: Any) -> None: ...

class HueCorrect:
    """Adjust hue, saturation, and value with a curve"""
    def __init__(self, Fac: float = ..., Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class HueSat:
    """Apply a color transformation in the HSV color model"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Hue: float = ..., Saturation: float = ..., Value: float = ..., Fac: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class IDMask:
    """Create a matte from an object or material index pass"""
    def __init__(self, index: int, use_antialiasing: bool, ID_value: float = ...) -> None: ...
    def Alpha(self) -> float: """Alpha"""

class Image:
    """Input image or movie file"""
    def __init__(self, image: Any, use_straight_alpha_output: bool, frame_duration: int, frame_start: int, frame_offset: int, use_cyclic: bool, use_auto_refresh: bool, layer: Any, view: Any) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Alpha(self) -> float: """Alpha"""

class Inpaint:
    """Extend borders of an image into transparent or masked regions"""
    def __init__(self, distance: int, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Invert:
    """Invert colors, producing a negative"""
    def __init__(self, invert_rgb: bool, invert_alpha: bool, Fac: float = ..., Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class Keying:
    """Perform both chroma keying (to remove the backdrop) and despill (to correct color cast from the backdrop)"""
    def __init__(self, screen_balance: Any, despill_factor: Any, despill_balance: Any, clip_black: Any, clip_white: Any, blur_pre: int, blur_post: int, dilate_distance: int, edge_kernel_radius: int, edge_kernel_tolerance: Any, feather_falloff: Any, feather_distance: int, Image: Tuple[float, float, float, float] = ..., Key_Color: Tuple[float, float, float, float] = ..., Garbage_Matte: float = ..., Core_Matte: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""
    def Edges(self) -> float: """Edges"""

class KeyingScreen:
    """Create plates for use as a color reference for keying nodes"""
    def __init__(self, clip: Any, tracking_object: str, smoothness: Any) -> None: ...
    def Screen(self) -> Tuple[float, float, float, float]: """Screen"""

class Kuwahara:
    """Apply smoothing filter that preserves edges, for stylized and painterly effects"""
    def __init__(self, variation: Any, use_high_precision: bool, uniformity: int, sharpness: Any, eccentricity: Any, Image: Tuple[float, float, float, float] = ..., Size: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Lensdist:
    """Simulate distortion and dispersion from camera lenses"""
    def __init__(self, use_projector: bool, use_jitter: bool, use_fit: bool, Image: Tuple[float, float, float, float] = ..., Distortion: float = ..., Dispersion: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Levels:
    """Compute average and standard deviation of pixel values"""
    def __init__(self, channel: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Mean(self) -> float: """Mean"""
    def Std_Dev(self) -> float: """Std Dev"""

class LumaMatte:
    """Create a matte based on luminance (brightness) difference"""
    def __init__(self, limit_max: Any, limit_min: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Matte(self) -> float: """Matte"""

class MapRange:
    """Map an input value range into a destination range"""
    def __init__(self, use_clamp: bool, Value: float = ..., From_Min: float = ..., From_Max: float = ..., To_Min: float = ..., To_Max: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class MapUV:
    """Map a texture using UV coordinates, to apply a texture to objects in compositing"""
    def __init__(self, alpha: int, filter_type: Any, Image: Tuple[float, float, float, float] = ..., UV: Tuple[float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class MapValue:
    """Scale, offset and clamp values"""
    def __init__(self, offset: Any, size: Any, use_min: bool, use_max: bool, min: Any, max: Any, Value: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class Mask:
    """Input mask from a mask datablock, created in the image editor"""
    def __init__(self, mask: Any, use_feather: bool, use_motion_blur: bool, motion_blur_samples: int, motion_blur_shutter: Any, size_source: Any, size_x: int, size_y: int) -> None: ...
    def Mask(self) -> float: """Mask"""

class Math:
    """Perform math operations"""
    def __init__(self, operation: Any, use_clamp: bool, Value1: float = ..., Value2: float = ..., Value3: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class MixRGB:
    """Blend two images together using various blending modes"""
    def __init__(self, blend_type: Any, use_alpha: bool, use_clamp: bool, Fac: float = ..., Image1: Tuple[float, float, float, float] = ..., Image2: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class MovieClip:
    """Input image or movie from a movie clip datablock, typically used for motion tracking"""
    def __init__(self, clip: Any) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Alpha(self) -> float: """Alpha"""
    def Offset_X(self) -> float: """Offset X"""
    def Offset_Y(self) -> float: """Offset Y"""
    def Scale(self) -> float: """Scale"""
    def Angle(self) -> float: """Angle"""

class MovieDistortion:
    """Remove lens distortion from footage, using motion tracking camera lens settings"""
    def __init__(self, clip: Any, distortion_type: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Normal:
    """Generate a normal vector and a dot product"""
    def __init__(self, Normal: Tuple[float, float, float] = ...) -> None: ...
    def Normal(self) -> Tuple[float, float, float]: """Normal"""
    def Dot(self) -> float: """Dot"""

class Normalize:
    """Map values to 0 to 1 range, based on the minimum and maximum pixel values"""
    def __init__(self, Value: float = ...) -> None: ...
    def Value(self) -> float: """Value"""

class OutputFile:
    """Write image file to disk"""
    def __init__(self, base_path: str, active_input_index: int, save_as_render: bool, Image: Tuple[float, float, float, float] = ...) -> None: ...

class Pixelate:
    """Reduce detail in an image by making individual pixels more prominent, for a blocky or mosaic-like appearance"""
    def __init__(self, pixel_size: int, Color: Tuple[float, float, float, float] = ...) -> None: ...
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class PlaneTrackDeform:
    """Replace flat planes in footage by another image, detected by plane tracks from motion tracking"""
    def __init__(self, clip: Any, tracking_object: str, plane_track_name: str, use_motion_blur: bool, motion_blur_samples: int, motion_blur_shutter: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Plane(self) -> float: """Plane"""

class Posterize:
    """Reduce number of colors in an image, converting smooth gradients into sharp transitions"""
    def __init__(self, Image: Tuple[float, float, float, float] = ..., Steps: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class PremulKey:
    """Convert to and from premultiplied (associated) alpha"""
    def __init__(self, mapping: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class RGB:
    """A color picker"""
    def __init__(self, ) -> None: ...
    def RGBA(self) -> Tuple[float, float, float, float]: """RGBA"""

class RGBToBW:
    """Convert RGB input into grayscale using luminance"""
    def __init__(self, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Val(self) -> float: """Val"""

class RLayers:
    """Input render passes from a scene render"""
    def __init__(self, scene: Any, layer: Any) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Alpha(self) -> float: """Alpha"""
    def Depth(self) -> float: """Depth"""
    def Normal(self) -> Tuple[float, float, float]: """Normal"""
    def UV(self) -> Tuple[float, float, float]: """UV"""
    def Vector(self) -> Tuple[float, float, float]: """Vector"""
    def Position(self) -> Tuple[float, float, float]: """Position"""
    def Deprecated1(self) -> Tuple[float, float, float, float]: """Deprecated"""
    def Deprecated2(self) -> Tuple[float, float, float, float]: """Deprecated"""
    def Shadow(self) -> Tuple[float, float, float, float]: """Shadow"""
    def AO(self) -> Tuple[float, float, float, float]: """AO"""
    def Deprecated3(self) -> Tuple[float, float, float, float]: """Deprecated"""
    def Deprecated4(self) -> Tuple[float, float, float, float]: """Deprecated"""
    def Deprecated5(self) -> Tuple[float, float, float, float]: """Deprecated"""
    def IndexOB(self) -> float: """IndexOB"""
    def IndexMA(self) -> float: """IndexMA"""
    def Mist(self) -> float: """Mist"""
    def Emit(self) -> Tuple[float, float, float, float]: """Emit"""
    def Env(self) -> Tuple[float, float, float, float]: """Env"""
    def DiffDir(self) -> Tuple[float, float, float, float]: """DiffDir"""
    def DiffInd(self) -> Tuple[float, float, float, float]: """DiffInd"""
    def DiffCol(self) -> Tuple[float, float, float, float]: """DiffCol"""
    def GlossDir(self) -> Tuple[float, float, float, float]: """GlossDir"""
    def GlossInd(self) -> Tuple[float, float, float, float]: """GlossInd"""
    def GlossCol(self) -> Tuple[float, float, float, float]: """GlossCol"""
    def TransDir(self) -> Tuple[float, float, float, float]: """TransDir"""
    def TransInd(self) -> Tuple[float, float, float, float]: """TransInd"""
    def TransCol(self) -> Tuple[float, float, float, float]: """TransCol"""
    def SubsurfaceDir(self) -> Tuple[float, float, float, float]: """SubsurfaceDir"""
    def SubsurfaceInd(self) -> Tuple[float, float, float, float]: """SubsurfaceInd"""
    def SubsurfaceCol(self) -> Tuple[float, float, float, float]: """SubsurfaceCol"""

class Rotate:
    """Rotate image by specified angle"""
    def __init__(self, filter_type: Any, Image: Tuple[float, float, float, float] = ..., Degr: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Scale:
    """Change the size of the image"""
    def __init__(self, space: Any, frame_method: Any, offset_x: Any, offset_y: Any, Image: Tuple[float, float, float, float] = ..., X: float = ..., Y: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class SceneTime:
    """Input the current scene time in seconds or frames"""
    def __init__(self, ) -> None: ...
    def Seconds(self) -> float: """Seconds"""
    def Frame(self) -> float: """Frame"""

class SepHSVA:
    """Deprecated"""
    def __init__(self, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def H(self) -> float: """H"""
    def S(self) -> float: """S"""
    def V(self) -> float: """V"""
    def A(self) -> float: """A"""

class SepRGBA:
    """Deprecated"""
    def __init__(self, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def R(self) -> float: """R"""
    def G(self) -> float: """G"""
    def B(self) -> float: """B"""
    def A(self) -> float: """A"""

class SepYCCA:
    """Deprecated"""
    def __init__(self, mode: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Y(self) -> float: """Y"""
    def Cb(self) -> float: """Cb"""
    def Cr(self) -> float: """Cr"""
    def A(self) -> float: """A"""

class SepYUVA:
    """Deprecated"""
    def __init__(self, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Y(self) -> float: """Y"""
    def U(self) -> float: """U"""
    def V(self) -> float: """V"""
    def A(self) -> float: """A"""

class SeparateColor:
    """Split an image into its composite color channels"""
    def __init__(self, mode: Any, ycc_mode: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Red(self) -> float: """Red"""
    def Green(self) -> float: """Green"""
    def Blue(self) -> float: """Blue"""
    def Alpha(self) -> float: """Alpha"""

class SeparateXYZ:
    """Split a vector into its individual components"""
    def __init__(self, Vector: Tuple[float, float, float] = ...) -> None: ...
    def X(self) -> float: """X"""
    def Y(self) -> float: """Y"""
    def Z(self) -> float: """Z"""

class SetAlpha:
    """Add an alpha channel to an image"""
    def __init__(self, mode: Any, Image: Tuple[float, float, float, float] = ..., Alpha: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Split:
    """Combine two images for side-by-side display. Typically used in combination with a Viewer node"""
    def __init__(self, axis: Any, factor: int, Image1: Tuple[float, float, float, float] = ..., Image2: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Stabilize:
    """Stabilize footage using 2D stabilization motion tracking settings"""
    def __init__(self, clip: Any, filter_type: Any, invert: bool, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class SunBeams:
    """Create sun beams based on image brightness"""
    def __init__(self, source: Any, ray_length: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Switch:
    """Switch between two images using a checkbox"""
    def __init__(self, check: bool, Off: Tuple[float, float, float, float] = ..., On: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class SwitchView:
    """Combine the views (left and right) into a single stereo 3D output"""
    def __init__(self, left: Tuple[float, float, float, float] = ..., right: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Texture:
    """Generate texture pattern from texture datablock"""
    def __init__(self, texture: Any, node_output: int, Offset: Tuple[float, float, float] = ..., Scale: Tuple[float, float, float] = ...) -> None: ...
    def Value(self) -> float: """Value"""
    def Color(self) -> Tuple[float, float, float, float]: """Color"""

class Time:
    """Generate a factor value (from 0.0 to 1.0) between scene start and end time, using a curve mapping"""
    def __init__(self, frame_start: int, frame_end: int) -> None: ...
    def Fac(self) -> float: """Fac"""

class Tonemap:
    """Map one set of colors to another in order to approximate the appearance of high dynamic range"""
    def __init__(self, tonemap_type: Any, key: Any, offset: Any, gamma: Any, intensity: Any, contrast: Any, adaptation: Any, correction: Any, Image: Tuple[float, float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class TrackPos:
    """Provide information about motion tracking points, such as x and y values"""
    def __init__(self, clip: Any, position: Any, frame_relative: int, tracking_object: str, track_name: str) -> None: ...
    def X(self) -> float: """X"""
    def Y(self) -> float: """Y"""
    def Speed(self) -> Tuple[float, float, float]: """Speed"""

class Transform:
    """Scale, translate and rotate an image"""
    def __init__(self, filter_type: Any, Image: Tuple[float, float, float, float] = ..., X: float = ..., Y: float = ..., Angle: float = ..., Scale: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Translate:
    """Offset an image"""
    def __init__(self, interpolation: Any, use_relative: bool, wrap_axis: Any, Image: Tuple[float, float, float, float] = ..., X: float = ..., Y: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class ValToRGB:
    """Map values to colors with the use of a gradient"""
    def __init__(self, Fac: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Alpha(self) -> float: """Alpha"""

class Value:
    """Input numerical values to other nodes in the node graph"""
    def __init__(self, ) -> None: ...
    def Value(self) -> float: """Value"""

class VecBlur:
    """Uses the vector speed render pass to blur the image pixels in 2D"""
    def __init__(self, samples: int, speed_min: int, speed_max: int, factor: Any, use_curved: bool, Image: Tuple[float, float, float, float] = ..., Z: float = ..., Speed: Tuple[float, float, float] = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""

class Viewer:
    """Visualize data from inside a node graph, in the image editor or as a backdrop"""
    def __init__(self, use_alpha: bool, ui_shortcut: int, Image: Tuple[float, float, float, float] = ..., Alpha: float = ...) -> None: ...

class Zcombine:
    """Combine two images using depth maps"""
    def __init__(self, use_alpha: bool, use_antialias_z: bool, Image1: Tuple[float, float, float, float] = ..., Z1: float = ..., Image2: Tuple[float, float, float, float] = ..., Z2: float = ...) -> None: ...
    def Image(self) -> Tuple[float, float, float, float]: """Image"""
    def Z(self) -> float: """Z"""

