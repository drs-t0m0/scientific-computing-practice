# 多次元配列の結合を行うオブジェクトnp.c_とnp.r_の使い方

特に何も指定しない場合は、np.r_はhstack、np.c_はvstackと同様の使い方をする

## np.r_

特に結合の様式を指定しない場合、np.r_に含まれる配列はaxis=0の方向に結合する  
これはnp.hstack関数と同じ機能

スライス表記によって1次元配列を作る

```
start:stop:step
```

デフォルトの値として、start=1、step=1