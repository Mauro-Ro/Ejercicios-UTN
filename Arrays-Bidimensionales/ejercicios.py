from funcionesmenu import alta_producto, baja_producto, modificar_producto


gondola = [
          [[None, 0], ["botellas", 3], [None, 0], ["frascos", 8], [None, 0]],
          [[None, 0], [None, 0], ["fideos", 4], [None, 0], [None, 0]],
          [["choclo", 2], [None, 0], [None, 0], ["leche", 6], [None, 0]]                        
          ]




if __name__ == '__main__':
  alta_producto("papas fritas",2 , gondola)
  alta_producto("fritas",2 , gondola)
  # for fila in gondola:
  #   for elemento in fila:
  #     print(elemento, end="\t")
  #   print()