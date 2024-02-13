let gameState = {}

const config = {
    type: Phaser.AUTO,
    width: 450,
    height: 450,
    scene: {
        create
    },
    scale: {autoCenter: Phaser.Scale.CENTER_BOTH}
}

function preload () {
    this.load.image("characterboxoutline", "./assets/ui/characterboxoutline.png");
    this.game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
    this.game.scale.pageAlignHorizontally = true;
    this.game.scale.pageAlignVertically = true;
}

function create () {
    this.add.image(0, 0, "characterboxoutline");


}

function update () {

}

const game = new Phaser.Game(config);