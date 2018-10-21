class Settlement < ApplicationRecord

  def get_lai
    LaiService.new
  end

end
