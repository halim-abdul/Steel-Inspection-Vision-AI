#include <algorithm>
#include <vector>

void normalize_u8(const std::vector<unsigned char>& in, std::vector<float>& out){
    out.resize(in.size());
    std::transform(in.begin(), in.end(), out.begin(), [](unsigned char v){ return static_cast<float>(v)/255.0f; });
}
