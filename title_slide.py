from pptx import Presentation

'''Cím és alcím diagramm'''

def title(item,slide,pres):
    title=slide.shapes.title
    subtitle=slide.placeholders[1]
    title.text = item['title']
    subtitle.text = item['content']
    return(slide)