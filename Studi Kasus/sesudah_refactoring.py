from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    sks_taken: int
    prerequisites_met: bool

class IValidationRule(ABC):
    @abstractmethod
    def validate(self, student: Student) -> bool:
        pass

class SksLimitRule(IValidationRule):
    def validate(self, student: Student) -> bool:
        if student.sks_taken > 24:
            print(f"Gagal: SKS {student.sks_taken} melebihi batas (Maks 24).")
            return False
        return True

class PrerequisiteRule(IValidationRule):
    def validate(self, student: Student) -> bool:
        if not student.prerequisites_met:
            print("Gagal: Prasyarat mata kuliah belum terpenuhi.")
            return False
        return True

class JadwalBentrokRule(IValidationRule):
    def validate(self, student: Student) -> bool:
        print("Info: Mengecek jadwal... Tidak ada bentrok.")
        return True

class RegistrationService:
    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules

    def register_student(self, student: Student):
        print(f"--- Mulai Validasi: {student.name} ---")
        
        for rule in self.rules:
            if not rule.validate(student):
                print("Hasil: Registrasi Ditolak.\n")
                return False
        
        print("Hasil: Registrasi Diterima.\n")
        return True

if __name__ == "__main__":
    mahasiswa = Student("Siti", 20, True)

    daftar_aturan = [
        SksLimitRule(),
        PrerequisiteRule(),
        JadwalBentrokRule() 
    ]

    service = RegistrationService(daftar_aturan)
    service.register_student(mahasiswa)