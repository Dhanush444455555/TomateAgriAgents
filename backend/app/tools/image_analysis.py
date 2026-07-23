"""Image Analysis Tool - Runs ML model inference for agent reasoning."""
from app.ml_models.growth_stage_model import GrowthStageModel
from app.ml_models.disease_detection_model import DiseaseDetectionModel


class ImageAnalysisTool:
    """Runs ML model inference on crop images.
    
    Used by: GrowthStageAgent, DiseaseDetectionAgent
    Returns: model predictions with confidence scores.
    """
    
    name = "image_analysis"
    description = "Analyze a crop image for growth stage classification or disease detection"
    
    def __init__(self):
        self._growth_model = None
        self._disease_model = None
    
    @property
    def growth_model(self):
        if self._growth_model is None:
            self._growth_model = GrowthStageModel()
        return self._growth_model
    
    @property
    def disease_model(self):
        if self._disease_model is None:
            self._disease_model = DiseaseDetectionModel()
        return self._disease_model
    
    async def detect_growth_stage(self, image_data: bytes) -> dict:
        """Classify the growth stage from a crop image."""
        try:
            result = self.growth_model.predict(image_data)
            return {"success": True, "prediction": result, "model": "MobileNetV2-TomatoStage"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    async def detect_diseases(self, image_data: bytes) -> dict:
        """Detect diseases/pests from a crop image."""
        try:
            result = self.disease_model.predict(image_data)
            return {"success": True, "detections": result, "model": "YOLOv8-TomatoDisease"}
        except Exception as e:
            return {"success": False, "error": str(e)}
