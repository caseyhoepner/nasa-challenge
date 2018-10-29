require 'rails_helper'

describe WaterCondition, type: :model do
  describe 'Relationships' do
    it { should belong_to(:settlement)}
  end
end
