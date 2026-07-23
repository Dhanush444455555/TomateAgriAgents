"""Soil Sensor Tool - Fetches IoT sensor readings for agent reasoning."""
from sqlalchemy.orm import Session
from app.db.session import get_session


class SoilSensorTool:
    """Fetches latest IoT sensor readings from the database.
    
    Used by: SoilIrrigationAgent, NutrientAgent
    Returns: soil moisture, temperature, EC, pH readings.
    """
    
    name = "soil_sensor"
    description = "Fetch latest soil sensor readings (moisture, temperature, EC, pH) for a farm"
    
    async def execute(self, farm_id: str) -> dict:
        """Fetch latest sensor readings from database."""
        # TODO: Connect to real IoT sensor data pipeline (MQTT/HTTP)
        # Placeholder: returns from SensorReading table
        try:
            # Will query SensorReading model once DB is implemented
            return {
                "success": True,
                "readings": {
                    "soil_moisture_pct": None,
                    "soil_temperature_c": None,
                    "electrical_conductivity": None,
                    "ph": None,
                    "timestamp": None,
                },
                "source": "IoT Sensor Network",
                "note": "No sensor data available — using manual input from farmer"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
