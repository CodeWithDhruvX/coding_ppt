const originalSlides = [...];  // paste first JSON here
const updatedSlides = [...];   // paste second JSON here

// Create a lookup map from the second JSON for quick access
const updatedMap = new Map();
updatedSlides.forEach(slide => {
  updatedMap.set(slide.title, slide);
});

const finalSlides = originalSlides.map(slide => {
  if (updatedMap.has(slide.title)) {
    const updated = updatedMap.get(slide.title);
    return {
      ...slide,
      content: updated.content,
      slide_type: updated.slide_type
    };
  }
  return slide; // keep original if no update found
});

console.log(JSON.stringify(finalSlides, null, 2));
