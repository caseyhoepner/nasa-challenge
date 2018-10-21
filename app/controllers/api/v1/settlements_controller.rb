class SettlementsController < ActionControlelr::API

  def index
    settlements = Settlement.all
    vegetation = settlements.get_lai
    render json: settlements
  end

end