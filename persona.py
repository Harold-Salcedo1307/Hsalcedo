class Persona:
    def __init__(
        self, id_persona: int, nombre: str, id_genero: int, genero_str: str
    ):
        self.id_persona = id_persona
        self.nombre = nombre
        self.id_genero = id_genero
        self.genero_str = genero_str


class Estudiante(Persona):

    def __init__(
        self, id_persona: int, nombre: str, id_genero: int, genero_str: str
    ):
        super().__init__(id_persona, nombre, id_genero, genero_str)
        self.examenes = [] # Lista de tuplas/diccionarios: {'materia': str, 'id_materia': int, 'nota': float}

    def agregar_examen(self, id_materia: int, materia_str: str, nota: float):
        self.examenes.append(
            {"id_materia": id_materia, "materia": materia_str, "nota": nota}
        )

    def contarRegulares() -> int:
 
def examenes_sobre_promedio(self) -> int:
        todas_las_notas = [
            ex["nota"]
            for est in self.estudiantes.values()
            for ex in est.examenes
        ]
        if not todas_las_notas:
            return 0
        promedio = sum(todas_las_notas) / len(todas_las_notas)
        return sum(1 for nota in todas_las_notas if nota > promedio)

    def contar_regulares_total(self) -> int:
        # Requisito: Exámenes con rango (2.5 - 3.5)
        total_regulares = 0
        for est in self.estudiantes.values():
            for ex in est.examenes:
                if 2.5 < ex["nota"] < 3.5:
                    total_regulares += 1
        return total_regulares

    def materia_mas_reprobados(self) -> str:
        reprobados = {m_id: 0 for m_id in self.MATERIAS.keys()}
        for est in self.estudiantes.values():
            for ex in est.examenes:
                if ex["nota"] < 3.0:
                    reprobados[ex["id_materia"]] += 1

        # Si hay empate, prioriza el requerimiento o la salida esperada
        id_materia_max = max(reprobados, key=reprobados.get)
        return self.MATERIAS[id_materia_max]

    def mejor_estudiante_materia(self, id_materia: int) -> str:
        mejor_nota = -1.0
        mejor_estudiante = ""

        for est in self.estudiantes.values():
            for ex in est.examenes:
                if ex["id_materia"] == id_materia and ex["nota"] > mejor_nota:
                    mejor_nota = ex["nota"]
                    mejor_estudiante = est.nombre

        return mejor_estudiante
