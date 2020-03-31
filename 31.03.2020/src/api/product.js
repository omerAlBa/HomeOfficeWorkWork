"use strict"

import axios from "axios"
const auth = {
  username: "f30b8Dr9qFteNLSfCtaOIQX1SHHJSxOIrwfb87Vo"
}

export async function search(term) {
  const response = await axios
    .post("https://api.nal.usda.gov/fdc/v1/search", {
      generalSearchInput: term
    }, {auth})
    return response.data['foods']
}

export async function info(fdcId) {
  const response = await axios
    .get("https://api.nal.usda.gov/fdc/v1/" + fdcId, {auth})
    return response.data
}

