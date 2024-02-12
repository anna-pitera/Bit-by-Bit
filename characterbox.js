let gameState = {}

const config = {
    type: Phaser.AUTO,
    width: 450,
    height: 450,
    scene: {
        create
    }
}

function preload () {
    this.load.image("characterboxoutline", "./assets/ui/characterboxoutline.png");
}

function create () {
    this.add.image(0, 0, "characterboxoutline");


}

function update () {

}

const game = new Phaser.Game(config);