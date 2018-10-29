class Api::V1::SettlementsController < ApplicationController

  def index
    settlements = Settlement.all
    # conn = Faraday.new(:url => 'https://gateway.watsonplatform.net/compare-comply/api/v1/element_classification?version=2018-08-24&file=@../../../public/aqueduct_global_maps_21.pdf;type=application/pdf&apikey=jGP5iW6qFY7xpxlJXJyxBLps2XQz3DPVLMnMAqSzf76v') 
    # response = conn.post do |req|
    #   req.url '/settlements'
    #   req.headers['Content-Type'] = 'application/json'
    # end
    # getting parsed PDF -> JSON is a WIP. Look at Compare Comply docs for more information.
  end

end