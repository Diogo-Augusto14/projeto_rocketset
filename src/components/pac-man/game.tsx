useEffect(() => {
  // Inicializa a instância
  const k = kaplay({
    width: 640,
    height: 640,
    background: "#0004ff",
    scale: 1,
  });

  // Cria o objeto do jogo
  const obj = k.add([
    k.rect(32, 32),
    k.pos(10, 20),
    "shape",
  ]);

  // Registra os eventos de controle fora do k.add() e usando 'k.'
  k.onKeyDown("right", () => {
    obj.move(200, 0);
  });

}, []);