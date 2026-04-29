from abc import ABC, abstractmethod

class Certificate(ABC):
    @abstractmethod
    def issue(self, student_name: str):
        pass

class BasicCertificate(Certificate):
    def issue(self, student_name: str):
        return f"📄 Basic Certificate issued to {student_name}"

class PremiumCertificate(Certificate):
    def issue(self, student_name: str):
        return f"🏆 Premium Certificate with badge issued to {student_name}"

class CertificateFactory(ABC):
    """Factory Method - lets subclasses decide which class to instantiate"""
    @abstractmethod
    def create_certificate(self) -> Certificate:
        pass

class BasicAcademyFactory(CertificateFactory):
    def create_certificate(self) -> Certificate:
        return BasicCertificate()

class PremiumAcademyFactory(CertificateFactory):
    def create_certificate(self) -> Certificate:
        return PremiumCertificate()