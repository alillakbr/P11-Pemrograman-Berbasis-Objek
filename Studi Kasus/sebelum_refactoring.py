from dataclasses import dataclass

@dataclass
class Student:
    name: str
    sks_taken: int
    prerequisites_met: bool

class SistemRegistrasi:
    def register_student(self, student: Student):
        print(f"Memproses registrasi untuk {student.name}...")

        if student.sks_taken > 24:
            print(f"Gagal: SKS {student.sks_taken} melebihi batas 24.")
            return False

        if not student.prerequisites_met:
            print("Gagal: Prasyarat mata kuliah belum terpenuhi.")
            return False

        print("Sukses: Registrasi diterima.")
        return True

if __name__ == "__main__":
    maba = Student("Budi", 25, True) 
    sistem = SistemRegistrasi()
    sistem.register_student(maba)