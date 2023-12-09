import { Particle, Effect } from './PIXLIB/script.js'

window.addEventListener('load',() => {

    const canvas = document.querySelector('.canvas1')
    const ctx1 = canvas.getContext('2d')
    const canvas2 = document.querySelector('.canvas2')
    const ctx2 = canvas.getContext('2d')
    
    
    const image= document.querySelector('.image1')
    const image2 = document.querySelector('.image2')

    const  effect1 = new Effect(canvas, ctx1, canvas.clientHeight, canvas.clientWidth, image)
    effect1.Init(ctx1)
    effect1.togglePhysics()
    
    const effect2 = new Effect(canvas2, ctx2, canvas2.clientHeight, canvas2.clientWidth, image2)
    effect2.Init(ctx2)
    effect2.togglePhysics()
    // effect2.togglePhysics()
    // effect1.togglePhysics()
    
    

    // const animate = (ctx, effect ,cnv) =>{
    //     ctx.clearRect(0, 0, cnv.width, cnv.height) // prevent trailing particles 
    //     // effect1.drawImage(ctx)
    //     effect.drawEffect(ctx)
    //     // effect.drawAsciiEffect(ctx) // for ascii
    //     effect.update()
    //     requestAnimationFrame(animate)
       
    // }
    
    
    // animate(ctx, effect1, canvas)
    // animate(ctx2, effect2, canvas2)

    

const animate = (ctxs, effects, canvases) => {
  

  // ctxs.forEach(ctx =>{
  //   ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  // })

  effects.forEach((effect, index) => {
    const canvas = canvases[index];
    const effectCtx = canvas.getContext('2d');
    effectCtx.clearRect(0, 0, effectCtx.canvas.clientWidth, effectCtx.canvas.clientHeight)
    effect.drawEffect(effectCtx);
    effect.update();
  });

  

  requestAnimationFrame(() => animate(ctxs, effects, canvases));
};

// Create instances of the Effect class


// Specify the corresponding canvases for each effect


// Call the animate function with the effects and canvases arrays
animate([], [effect1, effect2], [canvas, canvas2]);

})
