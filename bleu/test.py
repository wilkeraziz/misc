from grasp.loss.fast_bleu import doc_bleu

hypothesis = 'the two dogs bark'.split()
references = ['the two dogs barked'.split(), 'two dogs bark'.split()]
# I am using doc bleu here, but my document contains just one sentence ;)
bleu, pn, bp = doc_bleu(hyps=[hypothesis], 
        refsets=[references],
        max_order=4, 
        smoothing=1.0)  # BLEU-4 with +1 smoothing

print('BLEU={0} Pn={1} BP={2}'.format(bleu, pn, bp))
