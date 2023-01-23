from main import db


class Empresa(db.Model):

    __tablename__ = 'Empresa'

    cnpj_empresa = db.Column(db.String(20), primary_key=True)
    nome_empresa = db.Column(db.String(45), nullable=False)
    situacao_empresa = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name



class Filial(db.Model):

    __tablename__ = 'Filial'

    id_filial = db.Column(db.Integer, primary_key=True)
    nome_filial = db.Column(db.String(45), nullable=False)
    situacao_filial = db.Column(db.String(45), nullable=False)
    Empresa_cnpj_empresa = db.Column(db.String(20), db.ForeignKey("Empresa.cnpj_empresa"))

    def __repr__(self):
        return '<Name %r>' % self.name



class Admin(db.Model):

    __tablename__ = 'Admin'

    id_admin = db.Column(db.String(20), primary_key=True)
    usuario_admin = db.Column(db.String(45), nullable=False)
    senha_admin = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


