from aluno import Aluno
from disciplina import Disciplina

# criar 1 aluno
aluno1 = Aluno("João","123456","Ciencia da Computação")

# criar 1 disciplina
sers = Disciplina("Soluções Renováveis", "Tritiack")
cs = Disciplina("Computer Science", "Lucas")
# print(cs.professor)
# sers.exibir_infos()

# matriular o aluno nas disciplinas

aluno1.matricular(sers)
aluno1.matricular(cs)
# print(aluno1.disciplinas[0].professor)

# adicionar notas do aluno referente as disciplinas

aluno1.adicionar_notas(sers, 10)
aluno1.adicionar_notas(sers, 8)
aluno1.adicionar_notas(cs, 5)
aluno1.adicionar_notas(cs, 3)
# print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(sers))
print(aluno1.calcular_media_g())






