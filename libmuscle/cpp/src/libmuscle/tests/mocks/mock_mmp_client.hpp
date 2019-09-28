#pragma once

#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

#include <libmuscle/logging.hpp>

#include <ymmsl/model.hpp>
#include <ymmsl/identity.hpp>
#include "ymmsl/settings.hpp"


namespace libmuscle {

class MockMMPClient {
    public:
        MockMMPClient(std::string const & location);

        void submit_log_message(LogMessage const & message);

        ymmsl::Settings get_settings();

        void register_instance(
                ::ymmsl::Reference const & name,
                std::vector<std::string> const & locations,
                std::vector<::ymmsl::Port> const & ports);

        auto request_peers(::ymmsl::Reference const & name) ->
            std::tuple<
                std::vector<::ymmsl::Conduit>,
                std::unordered_map<::ymmsl::Reference, std::vector<int>>,
                std::unordered_map<::ymmsl::Reference, std::vector<std::string>>
            >;

        void deregister_instance(::ymmsl::Reference const & name);

        static void reset();

        static int num_constructed;
        static std::string last_location;
};

using MMPClient = MockMMPClient;

}

