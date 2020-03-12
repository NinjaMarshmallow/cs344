(let ((g (* 2 (or (gethash word good) 0)))
      (b (or (gethash word bad) 0)))
   (unless (< (+ g b) 5)
        (max .01
          (min .99 (float (/ (min 1 (/ b nbad))
                             (+ (min 1 (/ g ngood))   
                                (min 1 (/ b nbad))
                             )
                          )
                   )
          )
        )
    )
)

if (g + b > 5) {
    result = null
    let nBadMin = min(1, b / nbad)
    let nAllMin = min(1, g / ngood) + min(1, b / nbad)
    let percentBad = nBadMin / nAllMin
    probSpam = min(.99, percentBad)
    result = max(.01, probSpam)
    return result

}