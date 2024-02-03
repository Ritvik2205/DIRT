import React from 'react'
import openai from 'openai'

export default function Image() {

  async function createImage() {
    const response = await openai.createImage({
      model: "dall-e-3",
      prompt: "a white siamese cat",
      n: 1,
      size: "1024x1024",
    });
    const image_url = response.data.data[0].url;
    return image_url
  }


  return (
    <div>image_url</div>
  )
}
