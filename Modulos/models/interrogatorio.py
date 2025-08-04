from typing import Dict, Any


class Interrogatorio:
    def __init__(self):
        self.data: Dict[str, Dict[str, Any]] = {
            "1. Identificação": {},
            "2. Histórico de Saúde": {},
            "3. Sono": {},
            "4. Apetite e digestão": {},
            "5. Sede": {},
            "6. Evacuação e urina": {},
            "7. Saúde Reprodutiva": {},
            "8. Emoções predominantes": {},
            "9. Termorregulação e sudorese": {},
            "10. Dor": {},
            "11. Inspeção da língua e pulso": {},
            "12. Estações e horários de piora": {},
            "Interpretação final": {}
        }

        self.sexo_value = None

    def update_section(self, section: str, field: str, value: Any):
        self.data[section][field] = value

    def set_sexo(self, value: str):
        self.sexo_value = value
        self.data["1. Identificação"]["Sexo"] = value
